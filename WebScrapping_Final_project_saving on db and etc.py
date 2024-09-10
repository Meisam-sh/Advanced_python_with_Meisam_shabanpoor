### haminghadresho toonestam benevisam. kheili talash kardam . 
### az 35 nomreye in soal dar hadde 20 nomre ham bedid govahi ro begiram alii mishe
import mysql.connector 
import random
import asyncio  
import aiohttp  
import time 
import requests
import re
from bs4 import BeautifulSoup
########################################################
##################### this finction gets url and return soup of its html code
def soup_maker(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    return soup
###########################################################
###################this function gets soup and find title of all homes and returns a list of titles
def find_titles(soup):
    title_list=[]
    home_titles=soup.find_all('h2',class_='kt-post-card__title')
    for title in home_titles[:min(200, len(home_titles))]:  
        #print(title.get_text()) 
        title_list.append(title.get_text())
    return title_list
###########################################################
###################this function gets soup and find title of all homes and returns a list of price
def find_price(soup):
    price_list=[]
    home_prices=soup.find_all('div',class_='kt-post-card__description')
    #print(home_prices)
    for price in home_prices[:min(200, len(home_prices))]:  
        price_data=price.get_text()
        pattern=r'\d{1,3}(,\d{3})*'
        result=re.search(pattern,price_data).group() 
        cleaned_result=int(result.replace(',',''))
        price_list.append(cleaned_result)
        #print(cleaned_result)
    return price_list
#####################################################
##########################this function find all links of items and make a list of them
def find_item_link(soup):  
    link_list = []  
    item_links = soup.find_all('a')  # استخراج تمام تگ‌های <a>  
    
    for link in item_links:  
        href = link.get('href')  # دریافت لینک از تگ‌های <a>  
        if href and '/v/' in href:  # اگر href موجود باشد  
            #print(href)  # چاپ لینک در هر سطر  
            link_list.append(href)  # اضافه کردن لینک به لیست  
    
    return link_list  # بازگشت به لینک‌ها پس از اتمام حلقه
####################################################################
#############################Open each link########################
##########################################
semaphore = asyncio.Semaphore(50)  # حداکثر 50 درخواست همزمان  
async def fetch(session, url):  
    try:  
        async with semaphore: 
            async with session.get(url) as response:  
                if response.status == 200:  
                    html = await response.text()  
                    return html  
                elif response.status == 429:  
                    print(f'Rate limited for {url}. Waiting...')  
                    await asyncio.sleep(random.uniform(1, 5))  # انتظار تصادفی بین 1 تا 5 ثانیه  
                    return await fetch(session, url)  # دوباره تلاش کنید  
                else:  
                    print(f'Failed to open {url}, status code: {response.status}')  
                    return None  
    except Exception as e:  
        print(f'An error occurred while trying to open {url}: {e}')  
        return None  

async def parse_parking_info(html):  
    if html:  
        soup = BeautifulSoup(html, 'html.parser')  
        parking = soup.find_all('td', string=lambda x: x and 'پارکینگ' in x)  
        if parking:  
            if 'ندارد' in parking[0].text:  
                return 0  
            else:  
                return 1  
    return None  

async def open_each_links(links):  
    results = []  
    async with aiohttp.ClientSession() as session:  
        tasks = []  

        for url in links:  
            full_url = f'https://divar.ir{url}'  
            tasks.append(fetch(session, full_url))  
            await asyncio.sleep(0.5)  # انتظار نیم ثانیه بین اضافه کردن هر URL  

        responses = await asyncio.gather(*tasks)  

        for html in responses:  
            parking_info = await parse_parking_info(html)  
            results.append(parking_info)  

    return results  
# لیست لینک‌ها برای تست  
# اجرای کد به صورت همزمان  

###############################################################
############# function to connect to database named advancedpythonproject
def connect_to_db(db_name):  
    mydb = mysql.connector.connect(  
        host="localhost",  
        user="sa",  
        password="14001003Sofia_",  
        database=db_name,  
        auth_plugin='caching_sha2_password'  
    )  
    
    if mydb.is_connected():  
        #print("you are connected")  
        cursor = mydb.cursor()  
        return cursor, mydb  
    else:  
        #print("you are still not connected")  
        return None, None  
########################################################
####################### read data from table Home
def read_from_db(cursor):  
    cursor.execute("SELECT * FROM home")  
    result = cursor.fetchall()  
    for row in result:  
        print(row)  
########################################################
#####################write data in home table
def write_in_db(data,cursor):  
    sql = "INSERT INTO home (title, meterage, numberOfRooms, has_parking, address, price) VALUES (%s, %s, %s,%s, %s, %s)"  
    val = (data[1], data[2], data[3], data[4], data[5], data[6])
    cursor.execute(sql,val)
    db.commit()
########################################################
url='https://divar.ir/s/rasht/buy-residential'
soup=soup_maker(url)
title_list=find_titles(soup)
price_list=find_price(soup)
links=find_item_link(soup)
open_links = asyncio.run(open_each_links(links))  
db_name = "advancedpythonproject"  
cursor, db = connect_to_db(db_name)  
n=len(price_list)
#print(n)
for i in range(len(title_list)):
   data=[1,title_list[i], 80, 2, 0, 'lakan rasht', price_list[i]]
   write_in_db(data,cursor)
if cursor:  
    cursor.close()  
if db:  
    db.close()  