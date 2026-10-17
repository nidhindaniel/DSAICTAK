"""Beer alcohol regression assignment - Flask application.

The application downloads the assignment CSV from its public GitHub location,
compares tuned regressors by validation R2, and exposes the winning pipeline
through a small browser form.
"""

from __future__ import annotations

import io
import os
from dataclasses import dataclass
from functools import lru_cache

import pandas as pd
import plotly.express as px
import requests
from flask import Flask, render_template, request
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_URL = (
    "https://raw.githubusercontent.com/cksajil/DSAIRP25/main/"
    "datasets/beer-servings.csv"
)
TARGET = "total_litres_of_pure_alcohol"
NUMERIC_FEATURES = ["beer_servings", "spirit_servings", "wine_servings"]
CATEGORICAL_FEATURES = ["country", "continent"]
FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES

app = Flask(__name__)


@dataclass(frozen=True)
class ModelResults:
    model: Pipeline
    scores: dict[str, float]
    best_name: str
    dataframe: pd.DataFrame


def load_data() -> pd.DataFrame:
    """Load the linked assignment data, with a local file override for offline use."""
    local_path = os.environ.get("BEER_DATA_PATH")
    if local_path:
        data = pd.read_csv(local_path)
    else:
        response = requests.get(DATA_URL, timeout=30)
        response.raise_for_status()
        data = pd.read_csv(io.StringIO(response.text))

    required = set(FEATURES + [TARGET])
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Dataset is missing column(s): {', '.join(sorted(missing))}")
    return data.dropna(subset=[TARGET]).copy()


def make_preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            (
                "numeric",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                NUMERIC_FEATURES,
            ),
            (
                "categorical",
                Pipeline(
                    [("imputer", SimpleImputer(strategy="most_frequent")),
                     ("onehot", OneHotEncoder(handle_unknown="ignore"))],
                ),
                CATEGORICAL_FEATURES,
            ),
        ]
    )


def train_models(data: pd.DataFrame) -> ModelResults:
    """Tune two regressors and choose the higher hold-out R2 score."""
    X, y = data[FEATURES], data[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    candidates = {
        "Ridge Regression": (
            Ridge(),
            {"regressor__alpha": [0.1, 1.0, 10.0, 50.0]},
        ),
        "Random Forest": (
            RandomForestRegressor(random_state=42, n_jobs=-1),
            {
                "regressor__n_estimators": [150, 300],
                "regressor__max_depth": [None, 5, 10],
                "regressor__min_samples_leaf": [1, 2],
            },
        ),
    }
    fitted: dict[str, Pipeline] = {}
    scores: dict[str, float] = {}
    for name, (regressor, grid) in candidates.items():
        pipeline = Pipeline(
            [("preprocessor", make_preprocessor()), ("regressor", regressor)]
        )
        search = GridSearchCV(
            pipeline, grid, cv=5, scoring="r2", n_jobs=-1, refit=True
        )
        search.fit(X_train, y_train)
        fitted[name] = search.best_estimator_
        scores[name] = r2_score(y_test, search.best_estimator_.predict(X_test))

    best_name = max(scores, key=scores.get)
    # Refit selected tuned configuration using every row before deployment.
    fitted[best_name].fit(X, y)
    return ModelResults(fitted[best_name], scores, best_name, data)


@lru_cache(maxsize=1)
def get_results() -> ModelResults:
    return train_models(load_data())


def chart_html(data: pd.DataFrame) -> str:
    plot = px.scatter(
        data,
        x="beer_servings",
        y=TARGET,
        color="continent",
        hover_name="country",
        title="Beer servings and pure alcohol consumption",
        labels={"beer_servings": "Beer servings", TARGET: "Litres of pure alcohol"},
        template="plotly_white",
    )
    return plot.to_html(full_html=False, include_plotlyjs="cdn")


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        results = get_results()
    except (requests.RequestException, ValueError) as error:
        return render_template("error.html", error=str(error)), 503

    data = results.dataframe
    prediction = None
    submitted = {}
    if request.method == "POST":
        try:
            submitted = {field: request.form.get(field, "").strip() for field in FEATURES}
            numeric_values = {
                name: float(submitted[name]) for name in NUMERIC_FEATURES
            }
            if any(value < 0 for value in numeric_values.values()):
                raise ValueError("Serving values cannot be negative")
            row = pd.DataFrame(
                [{
                    "country": submitted["country"],
                    "continent": submitted["continent"],
                    **numeric_values,
                }]
            )
            prediction = round(float(results.model.predict(row)[0]), 2)
        except (TypeError, ValueError):
            prediction = "Please enter valid non-negative numeric values."

    return render_template(
        "index.html",
        countries=sorted(data.country.dropna().unique()),
        continents=sorted(data.continent.dropna().unique()),
        scores=results.scores,
        best_name=results.best_name,
        chart=chart_html(data),
        summary={"countries": data.country.nunique(), "average": round(data[TARGET].mean(), 2)},
        prediction=prediction,
        submitted=submitted,
    )


if __name__ == "__main__":
    app.run(debug=True)
