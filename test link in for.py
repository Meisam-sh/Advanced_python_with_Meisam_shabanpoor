import requests  
import re  

# لیستی از URLs که می‌خواهید باز کنید  
urls = [  
    'https://www.example.com',  
    'https://www.python.org',  
    'https://www.github.com'  
]  

# الگوی Regex که می‌خواهید در HTML جستجو کنید  
# به عنوان مثال، جستجوی تمام آدرس‌های ایمیل  
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  

# حلقه برای باز کردن هر URL  
for url in urls:  
    try:  
        # ارسال درخواست GET به URL  
        response = requests.get(url)  
        
        # بررسی وضعیت پاسخ  
        if response.status_code == 200:  
            print(f'Successfully opened {url}')  

            # جستجو در محتوای HTML با استفاده از Regex  
            matches = re.findall(pattern, response.text)  
            
            if matches:  
                print(f'Found {len(matches)} matches in {url}:')  
                for match in matches:  
                    print(f' - {match}')  
            else:  
                print(f'No matches found in {url}.')  
        else:  
            print(f'Failed to open {url}, status code: {response.status_code}')  
            
    except requests.exceptions.RequestException as e:  
        print(f'An error occurred while trying to open {url}: {e}')