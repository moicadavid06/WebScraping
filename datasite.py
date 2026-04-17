import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re

def main():
    
    url = "https://books.toscrape.com/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print("Fetching data...")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error accessing the website")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    prices = []

    
    for price in soup.find_all("p", class_="price_color"):
        text = price.get_text()
        try:
            value = float(re.findall(r"\d+\.\d+", text)[0])
            prices.append(value)
        except:
            continue

    if not prices:
        print("No data found!")
        return

    print(f"Found {len(prices)} products")
    print("Min price:", min(prices))
    print("Max price:", max(prices))
    print("Average price:", sum(prices) / len(prices))

    # Plot graph
    plt.figure()
    plt.plot(prices)
    plt.title("Book Prices")
    plt.xlabel("Product Index")
    plt.ylabel("Price (£)")

    # Save graph
    plt.savefig("prices_chart.png")
    print("Chart saved as prices_chart.png")

    plt.show()

if __name__ == "__main__":
    main()