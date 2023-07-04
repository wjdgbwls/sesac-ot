import os

data = "hello, world \asdfasdfafsn"

filepath='./data/'
filename="names.txt"
try:
    with open(filepath+filename,"w") as file:
      file.write(data)
except FileNotFoundError: 
    os.mkdir(filepath)

print("파일 쓰기 완료")

