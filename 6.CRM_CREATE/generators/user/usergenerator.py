import random
import pandas as pd
import datetime

class UserDataGenerator():
    
    def __init__(self, first_names_file,last_names_file): # 생성자
        self.first_names_file = first_names_file
        self.last_names_file = last_names_file
        self.data = []
        self.birth = []
        self.gender = []
        self.address = []
        self.cities = ['서울', '부산', '대구', '인천', '광주']
        self.gus = ['강남구', '강서구', '중구', '남구', '서구']
        self.streets = ['길', '로']
    #
    # 주소 생성
    #
    def generate_citys(self, num_people):
        city = random.choice(self.cities)
        gu = random.choice(self.gus)
        street = random.choice(self.streets)
        for i in range(num_people):
          road_number = random.randint(1, 100)
          road_number2 = random.randint(1, 100)
          add = f"{city} {gu} {road_number}{street} {road_number2}"
          self.address.append(add)
        return self.address 
    #
    # 파일 읽기
    #
    def file_read(self, file_path):
        with open(file_path, "rt", encoding='UTF8') as file:
            data = [line.strip() for line in file]
        return data
    #
    # 생년월일 생성
    #
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
    #
    # 이름 생성
    #

    def generate_name(self, num_people):
        frist_names = self.file_read(self.first_names_file)
        last_names = self.file_read(self.last_names_file)
        for _ in range(num_people):
            frist_name = random.choice(frist_names)
            last_name = random.choice(last_names)
            result_name = frist_name + last_name
            self.data.append(result_name)
        return self.data
    #
    # 성별 
    #
    def generate_gender(self, num_people):
        genders = ['남성', '여성']
        for _ in range(num_people):
            gender = random.choice(genders)
            self.gender.append(gender)
        return self.gender
    #
    # 데이터를 CSV로 저장
    #
    def save_to_csv_user(self):
        people = []
        for i in range(len(self.data)):
            people_data = {
                "이름": self.data[i],
                "생년월일": self.birth[i],
                "성별": self.gender[i],
                "도시": self.address[i]
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


user_generator = UserDataGenerator('../../texts/first_names.txt','../../texts/last_names.txt')
user_generator.generate_user_data(100)