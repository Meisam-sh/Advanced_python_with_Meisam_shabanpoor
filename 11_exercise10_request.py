from urllib import request
import csv
r=request.get("https://varzesh3.com")
res = urllib.request.urlopen("https://google.com")
data = res.read().decode('utf-8')
data

# Modify file path with double backslashes
with open('C:\\Users\\admin\\Desktop\\Python exercise\\Python Class\\Advanced\\Advancedurl.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([data])