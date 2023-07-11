import random
import pandas as pd
import datetime

class UserDataGenerator():
    
    def __init__(self, names_file, cities_file): # 생성자
        self.cities_file = cities_file
        self.names_file = names_file
        self.data = []
        self.birth = []
        self.gender = []
        self.cities = []
        
    def file_read(self, file_path):
        with open(file_path, "rt", encoding='UTF8') as file:
            data = [line.strip() for line in file]
        return data

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
        start_year = 1950
        end_year = datetime.datetime.now().year
        for _ in range(num_people):
            result_year = random.randint(start_year, end_year)
            result_month = random.randint(1, 12)
            result_day = random.randint(1, 28)
            birthdate = datetime.datetime(result_year, result_month, result_day)
            age = datetime.datetime.now().year - result_year
            self.birth.append(f'{birthdate.strftime("%Y년 %m월 %d일")} {age}살')
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
        df.to_csv("user.csv", index=False)

    def generate_user_data(self, num_people):
        self.generate_name(num_people)
        self.generate_birth(num_people)
        self.generate_gender(num_people)
        self.generate_citys(num_people)
        self.save_to_csv_user()
        print("CSV 파일이 생성되었습니다.")


user_generator = UserDataGenerator('../names.txt', '../cities.txt')
user_generator.generate_user_data(100000)