import csv
import random
data=[]
string1='names.txt'
def file_read(string1):
    print(string1)
    with open(string1, "rt",encoding='UTF8') as file: #r=read ,w = write ,a = append  whit as 는 내가 연파일을 =file이라고 부르겠다
      names_file= file.read().split(',')
    
      '''for item in names_file:
        file_name.append(item)
      print(names_file)'''
      return names_file
file_read(string1)


def generate_name(num_people):
    
    for _ in range(num_people):
        
        result_name = random.choice(file_read(string1))
        data.append(result_name)
    return data