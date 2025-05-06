import requests
from bs4 import BeautifulSoup
import json

# Example scraper function
def scrape_webtoons():
    url = "https://www.webtoons.com/en/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting titles (Modify this according to the site structure)
    titles = [a.text for a in soup.find_all('a', class_='card_item')][:10]
    
    # Save to JSON file
    data = [{"title": title, "language": "English"} for title in titles]
    with open('data/sample_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Data scraped and saved.")

if __name__ == "__main__":
    scrape_webtoons()