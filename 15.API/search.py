import json
import requests
import os
import sys

# curl "https://openapi.naver.com/v1/papago/n2mt" 
# -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" 
# -H "X-Naver-Client-Id: rl_WQXHbPLdAvIbmKJqf" 
# -H "X-Naver-Client-Secret: zJoH5SAkK5" 
# -d "source=ko&target=en&text=만나서 반갑습니다." -v


import urllib.request
client_id = "rl_WQXHbPLdAvIbmKJqf" # 개발자센터에서 발급받은 Client ID 값
client_secret = open('secret.txt','r').read() # 개발자센터에서 발급받은 Client Secret 값

encText = urllib.parse.quote("반갑습니다") #번역을 원하는 단어
data = "query" + encText
url = "https://openapi.naver.com/v1/search/book.json"

request = urllib.request.Request(url) #url에 request요청
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    data = json.loads(response_body)
    print(data['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)