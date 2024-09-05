import requests
from bs4 import BeautifulSoup
import re

url = 'https://divar.ir/s/rasht/auto'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

ads = soup.find_all('div', class_='kt-post-card')

for ad in ads:
    title = ad.find('h2', class_='kt-post-card__title').text
    price = ad.find('div', class_='kt-post-card__description').text.strip()

    # Check if the price is empty for tavafoghy
    if not re.search(r'\d', price):
        print(title)