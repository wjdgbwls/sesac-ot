import random
import pandas as pd
from classgenerate import File_read
import uuid
from datetime import datetime
#스타벅스 홍대8호점,스타벅스,부산 강남구 31로 50

class UserDataGenerator(File_read):
    
    def __init__(self, names_file, cities_file): #생성자
        self.cities_file = cities_file
        self.names_file = names_file
        self.data = []
        self.birth = []
        self.gender = []
        self.cities = []
        

    def generate_citys(self, num_people):
        cities = self.file_read(self.cities_file)
        for _ in range(num_people):
            result_city = random.choice(cities)
            self.cities.append(result_city)
        return self.cities



    def generate_name(self, num_people):
        names = self.file_read(self.names_file)
        for _ in range(num_people):
            result_name = random.choice(names)
            self.data.append(result_name)
        return self.data

    def generate_birth(self, num_people):
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        start_year = 1950
        end_year = 2023
        for _ in range(num_people):
            result_year = random.randint(start_year, end_year)
            result_birth = random.randint(1, 12)
            result_day = random.randint(1, 28)
            today = datetime.today().date()
            age = today.year - birthdate.year
            if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
                age -= 1
                self.birth.append(
                    f'{result_year}년 {result_birth}월 {result_day}일 {age}살'
            )
            #TODO 나이계산하기 윤년 검색해서
        return self.birth

    def generate_gender(self, num_people):
        genders = ['남성', '여성']
        for _ in range(num_people):
            gender = random.choice(genders)
            self.gender.append(gender)
        return self.gender

    def save_to_csv_user(self):
        people = []
        for i in range(len(self.data)):
            people_data = {
                "이름": self.data[i],
                "생년월일": self.birth[i],
                "성별": self.gender[i],
                "도시": self.cities[i]
            }
            people.append(people_data)
        df = pd.DataFrame(people)
        print(df)
        df.to_csv("user.csv", index=False)

    def generate_user_data(self, num_people):
        self.generate_name(num_people)
        self.generate_birth(num_people)
        self.generate_gender(num_people)
        self.generate_citys(num_people)
        self.save_to_csv_user()
        print("CSV 파일이 생성되었습니다.")



class ItemDataGenenator(File_read):
    item_Id = uuid.uuid4()
    def __init__(self, item_names_file, item_category_file, item_price_file): #생성자
      self.item_names_file = item_names_file
      self.item_category_file = item_category_file
      self.item_price_file = item_price_file
      self.item_name = []
      self.item_category =[]
      self.item_price = []

    def generate_item_name(self, num):
        #텍스트 파일에서 item 이름을 가져와라
        items = self.file_read(self.item_names_file)
        for _ in range(num):
            result_item = random.choice(items)
            self.item_name.append(result_item)
        return  self.item_name
    
    def generate_item_category(self, num, item_name):
        categorys = self.file_read(self.item_category_file)
        for category in categorys:
            if item_name == 'coffee':
                self.item_category.append('coffee')
            elif item_name == 'cake':
                self.item_category.append('cake')
            else:
                self.item_category.append('juice')
        return  self.item_category
        
    def generate_item_price(self, num):
        price = self.file_read(self.item_price_file)
        for _ in range(num):
            result_price = random.choice(price)
            self.item_price.append(result_price)
        return self.item_price
    
    def generate_item_data(self, num):
        self.generate_item_name(num)
        self.generate_item_category(num)
        self.generate_item_price(num)
        self.save_to_csv_item()
    
    
    def save_to_csv_item(self, num, test):
        item = []
        for i in range(num):
            item_data={
                "Item_Id": user_Id,
                "이름" : self.item_name[i],
                "종류" : self.item_category[i],
                "가격" : self.item_price[i]
            }
            item.append(item_data)
        df = pd.DataFrame(item)
        if test == 'console':
            print(df)
        elif test == 'csv':
            df.to_csv("item.csv", index=False)
        else:
            print('잘못입력했다 프로그램 종료')
        return
    


class File_read:
    def file_read(self, file_path):
        with open(file_path, "rt", encoding='UTF8') as file:
            data = file.read().split(', ')
            # TODO 공백없애기
        return data
    
class Generate_data_order(File_read):
     
     def generate_item_price(self, num):
        price = self.file_read(self.item_price_file)
        for _ in range(num):
            result_price = random.choice(price)
            self.item_price.append(result_price)
        return self.item_price
item_generator=ItemDataGenenator('item_names_file.txt','item_category_file.txt', 'item_price_file.txt')
#스타벅스 홍대8호점,스타벅스,부산 강남구 31로 50
# 클래스 인스턴스 생성
User_generator = UserDataGenerator("names.txt","cities.txt")
# 사용자 데이터 생성
User_generator.generate_user_data(10)
test= input('console 또는 csv중에 하나를 입력하세요: ')
item_generator.generate_item_data(10,test)
user_Id = uuid.uuid4()


#TODO 입력을 받아 실행하기...console or csv..
#파일을  로드함수로 만들고 

#
#Strawberry Cake,Cake,5500 이름,카테고리,가격
#Americano Coffee,Coffee,3000
#Id,OrderAt,StoreId,UserId"Coffee": {
    item={"Americano": 3000,
    "Latte": 4000,
    "Espresso": 2500,
    "Cappuccino": 4500,
    "Mocha": 5000
}
"Juice": {
    "Orange": 2000,
    "Apple": 2500,
    "Grape": 3000,
    "Pineapple": 3500,
    "Watermelon": 4000
},
"Cake": {
    "Chocolate": 6000,
    "Strawberry": 5500,
    "Vanilla": 5000,
    "Red Velvet": 6500,
    "Carrot": 6000
}
}