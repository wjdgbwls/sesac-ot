import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.pythonscraping.com/pages/page3.html',verify=False)

#print(data)
#print(data.text)

soup = BeautifulSoup(data.text, 'html.parser')

#print(soup)

gifts = soup.select('#giftList > tr')
#print(len(gifts))

my_gifts = gifts[1:]
print(len(my_gifts))

for n in my_gifts:
    #print(g)
    a_tag = n.select_one('a')
    print(a_tag['href'])