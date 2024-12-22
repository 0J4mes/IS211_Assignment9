# scraper_one.py

import requests
from bs4 import BeautifulSoup

def scrape_football_stats():
    url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming the CBS table has specific CSS selectors (update as necessary)
    table_rows = soup.select("table tbody tr")[:20]  # Limit to top 20 players

    print("Top 20 Players in Touchdowns:")
    print(f"{'Player':<20} {'Position':<10} {'Team':<10} {'Touchdowns':<10}")
    print("-" * 50)

    for row in table_rows:
        player = row.select_one('.PlayerName').text.strip()
        position = row.select_one('.Position').text.strip()
        team = row.select_one('.Team').text.strip()
        touchdowns = row.select_one('.Stat').text.strip()
        print(f"{player:<20} {position:<10} {team:<10} {touchdowns:<10}")

if __name__ == "__main__":
    print("Running scraper one...")
    scrape_football_stats()
