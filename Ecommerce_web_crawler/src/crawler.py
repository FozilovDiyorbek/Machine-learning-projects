import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

def run_crawler():
    url = "https://books.toscrape.com/"  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    for item in soup.select(".product_pod"):
        title = item.h3.a["title"]
        price = item.select_one(".price_color").text.replace("£", "")
        rating = item.p["class"][1] 

        price = price.replace("Â", "").replace("£", "").replace("$", "").replace(",", "").strip()
        products.append([title, float(price), rating])

    df = pd.DataFrame(products, columns=["title", "price", "rating"])
    os.makedirs("data/raw", exist_ok=True)
    filename = f"data/raw/products_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    print(f"{len(df)} products saved in {filename}")

if __name__ == "__main__":
    run_crawler()

