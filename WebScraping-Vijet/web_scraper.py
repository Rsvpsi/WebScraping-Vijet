import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# -----------------------------
# Product URLs
# -----------------------------
product_urls = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
]

# -----------------------------
# Target Price
# -----------------------------
target_price = 40

# -----------------------------
# Create Images Folder
# -----------------------------
os.makedirs("images", exist_ok=True)

for url in product_urls:

    print("=" * 60)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Product Title
    title = soup.find("h1").text

    # Price
    price_text = soup.find("p", class_="price_color").text

    price = float(price_text.replace("£", "").replace("Â", ""))

    # Image URL
    image = soup.find("img")

    image_url = urljoin(url, image["src"])

    # Download Image
    image_data = requests.get(image_url).content

    filename = os.path.join("images", title.replace("/", "_") + ".jpg")

    with open(filename, "wb") as f:
        f.write(image_data)

    # Display Details
    print("Title :", title)
    print("Price :", price)
    print("Image URL :", image_url)

    # Compare Price
    if price <= target_price:
        print("Result : Price is below target price")
    else:
        print("Result : Price is above target price")