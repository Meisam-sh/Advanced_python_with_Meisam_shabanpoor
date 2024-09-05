from urllib import request
import csv

url = "https://www.varzesh3.com/search?q=%D8%A8%D8%B1%D8%B2%DB%8C%D9%84"  # Replace this with the URL of the webpage you want to retrieve
response = request.urlopen(url)
html = response.read()
response.json()
# Write the HTML content to a CSV file with corrected file path
with open(r'C:\Users\admin\Desktop\Python exercise\Python Class\Advanced\url2.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([html.decode('utf-8')])