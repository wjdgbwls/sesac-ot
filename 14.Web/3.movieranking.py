import requests
from bs4 import BeautifulSoup

data = requests.get('https://movie.daum.net/ranking/reservation',verify=False)

soup = BeautifulSoup(data.text, 'html.parser')

ranking =soup.select('#mainContent > div > div.box_ranking > ol >li')

for rank in ranking:
    tag = rank('img')
    print(tag[0]['src'])