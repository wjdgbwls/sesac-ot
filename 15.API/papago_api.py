import os
import sys

import requests
import numpy 
def clova_face(filename):
    
  client_id = "rl_WQXHbPLdAvIbmKJqf"
  client_secret = open('secret.txt','r').read()
  # url = "https://openapi.naver.com/v1/vision/face" // 얼굴감지
  url = "https://openapi.naver.com/v1/vision/celebrity"
  files = {'image': open(filename, 'rb')}
  headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
  response = requests.post(url,  files=files, headers=headers)
  rescode = response.status_code
  if(rescode==200):
      print (response.text)
  else:
      print (response.text)

def my_opencv(filename):
   img_array = np.fromfile(filename, np.uint8)
   image = cv2.imdecode(img_array, cv2.IMREAD)
   cv2.rectangle(image,(10,10),(100,100),(0,0,255),2)
   #image = cv2.imread(filename)
   cv2.imshow('WindowName',image)
   cv2.waitKey(0)

if __name__ == "__main__":
  filename = '두환.jpg'
  # my_opencv()
  clova_face(filename)