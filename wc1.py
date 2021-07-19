import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.type06_headline')
    titles = ul.select('li > dl > dt:nth-child(2) > a')
    for title in titles:
        print(title.get_text())

else : 
    print(response.status_code)