# scraper_two.py

import requests
from bs4 import BeautifulSoup

def scrape_apple_stock():
    url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming Yahoo uses a specific table structure
    rows = soup.select("table tbody tr")

    print("Apple Stock Historical Prices:")
    print(f"{'Date':<15} {'Close Price':<10}")
    print("-" * 30)

    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 5:  # Ensure it's a valid data row
            date = cols[0].text.strip()
            close_price = cols[4].text.strip()
            print(f"{date:<15} {close_price:<10}")

if __name__ == "__main__":
    print("Running scraper two...")
    scrape_apple_stock()
