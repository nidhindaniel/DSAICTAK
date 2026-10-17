# Beer Alcohol Predictor

A Flask submission for the Beer Servings regression assignment. It predicts
`total_litres_of_pure_alcohol` from country, continent, and beverage-serving
counts.

## Assignment coverage

- Compares Ridge Regression and Random Forest Regression.
- Tunes both with 5-fold `GridSearchCV`.
- Selects the deployed model using hold-out R2 on an 80/20 split.
- Provides landing-page statistics, an interactive data infographic, three
  numeric inputs, and categorical dropdowns.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app app run --debug
```

The app downloads the provided CSV from GitHub on its first request. For an
offline run, download that CSV and set `BEER_DATA_PATH` to its full path.

## Deploy

Use `gunicorn app:app` as the start command on a Python web host. On Windows,
use `flask --app app run` for local development.
