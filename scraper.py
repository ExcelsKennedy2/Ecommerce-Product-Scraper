import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

products = []
prices = []
ratings = []
links = []

items = soup.find_all("article", class_="product_pod")

for item in items:

    name = item.h3.a["title"]

    price = item.find("p", class_="price_color").text

    rating = item.p["class"][1]

    link = item.h3.a["href"]

    products.append(name)
    prices.append(price)
    ratings.append(rating)
    links.append("https://books.toscrape.com/" + link)

df = pd.DataFrame({
    "Product": products,
    "Price": prices,
    "Rating": ratings,
    "Link": links
})

df.to_excel("products.xlsx", index=False)

print("Data exported successfully!")