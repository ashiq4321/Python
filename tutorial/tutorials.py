import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
url = 'https://coreyms.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
csv_file=open("E:/Fiverr/web scraping/tutorials.CSV",'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])
for article in soup.find_all('article'):
    headline=article.find('a').text
    description=article.find('div',class_="entry-content")
    desc=description.find('p').text
    try:
        link=description.find('iframe')['src']
        link=link.split('?')
    except Exception as e:
        link[0]="none"
    csv_writer.writerow([headline,desc,link[0]])
csv_file.close()
