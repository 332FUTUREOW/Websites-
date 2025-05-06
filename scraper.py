
# AI-Powered Web Scraper for Manhwa
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def fetch_manhwa_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h3')  # Update selector as needed
        return [title.a['title'] for title in titles if title.a]
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

def translate_titles(titles, src_lang="en", dest_lang="ar"):
    translator = Translator()
    translations = []
    for title in titles:
        translated = translator.translate(title, src=src_lang, dest=dest_lang).text
        translations.append((title, translated))
    return translations

def save_translations(translations, filename="translated_titles.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for original, translated in translations:
            file.write(f"Original: {original} | Translated: {translated}\n")
    print(f"Translations saved to {filename}")

if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"  # Example URL
    titles = fetch_manhwa_titles(url)
    if titles:
        translations = translate_titles(titles)
        save_translations(translations)
