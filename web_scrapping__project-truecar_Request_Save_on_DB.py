import requests
import sqlite3
import os
import re
from bs4 import BeautifulSoup

my_car = input()  # برای مثال Mercedes-benz
url = f'https://www.truecar.com/used-cars-for-sale/listings/{my_car}/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

car_prices = soup.find_all('h3', class_='heading-4')
car_miles = soup.find_all('div', class_='flex items-center truncate text-xs')
car_data = []

for i in range(min(20, len(car_prices))):
    price_text = car_prices[i].find(string=True)
    mileage_text = car_miles[i].find(string=True)
    price = re.search(r'\$(\d+,\d+)', price_text).group(1)
    mileage = re.search(r'\d+k\s*mi', mileage_text).group(0)

    car_info = {
        'model': my_car,
        'price': price,
        'mileage': mileage
    }

    car_data.append(car_info)
#############create database 
if not os.path.exists('d:\my_database.db'):
    open('my_database.db', 'a').close()

# اضافه کردن داده به پایگاه داده SQLite
conn = sqlite3.connect('d:\my_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS car_info 
                (id INTEGER PRIMARY KEY, model TEXT, price TEXT, mileage TEXT)''')

for car_info in car_data:
    cursor.execute("INSERT INTO car_info (model, price, mileage) VALUES (?, ?, ?)",
                   (car_info['model'], car_info['price'], car_info['mileage']))

conn.commit()
conn.close()