import bs4
import requests


def decode_secret_message(doc_url):
    # 1. Fetch document content
    response = requests.get(doc_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # 2. Parse table rows, extracting x, character, and y
    data = []
    max_x, max_y = 0, 0

    for row in soup.find_all("tr")[1:]:  # Skip header row
        cols = row.find_all("td")
        if len(cols) == 3:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())

            data.append((x, y, char))
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    # 3. Create grid populated with space characters
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # 4. Fill coordinates (y=0 at the bottom, so grid row index is max_y - y)
    for x, y, char in data:
        grid[max_y - y][x] = char

    # 5. Print the formatted secret message grid
    for row in grid:
        print("".join(row))


# Verification run:
decode_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)