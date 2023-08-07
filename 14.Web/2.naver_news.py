import requests
from bs4 import BeautifulSoup


def sportnew():
  data = requests.get('https://sports.news.naver.com/index', verify =False)
  soup = BeautifulSoup(data.text,'html.parser')

  news = soup.select('.today_list > li')
  url ='https://sports.news.naver.com/'
  for n in news:
      a_tag = n.select_one('a')
      print(a_tag['title'])

      # title = n.select_one('.title')
      # print(title.text)

      # strong = n.select_one('strong')
      # print(strong.text)

#미션3 헤드라인의 본문
def get_trend_land():
   data = requests.get('https://land.naver.com/news/')
   soup = BeautifulSoup(data.text, 'html.parser')

   content = soup.select('#content > div > div > div.section_group.NE\=a\:chl > ul > li ')

   for news in content:
      a_tags = news.select('a')
      print(a_tags[0].text,a_tags[1].text)

def get_naver_land():
   data = requests.get('https://land.naver.com/news/')
   soup = BeautifulSoup(data.text, 'html.parser')
   url = 'https://land.naver.com/'
   content = soup.select_one('#content')
   section = content.select_one('.section_group')
   headline =section.select('.list_type > li') 
   print(len(headline))
   for news in headline:
      a_tags = news.select('a')
      
      print(url+a_tags[1]['href'])
      print


if __name__ == "__main__":
  #sportnew()
  get_trend_land()
  #get_naver_land()