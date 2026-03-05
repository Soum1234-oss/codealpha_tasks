import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for q in soup.find_all("span", class_="text"):
    quotes.append(q.text)

for a in soup.find_all("small", class_="author"):
    authors.append(a.text)

data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

data.to_csv("quotes_dataset.csv", index=False)

print(data)