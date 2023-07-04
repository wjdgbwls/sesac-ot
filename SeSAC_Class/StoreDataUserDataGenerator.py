import random
import uuid
import pandas as pd
from classgenerate import File_read


class StoreDataGenerator(File_read):
    store_Id =uuid.uuid4()
    def __init__(self, store_file, cities_file, cities2_file, store_num_file):
        #부모 클래스인 UserDataGenerator의 초기화 메서드를 호출하는 코드입니다.
        
        #StoreDataGenerator 클래스에 새로운 속성인 store_file을 추가하는 코드입니다. 이 속성은 가게 데이터를 저장할 파일의 경로를 나타냅니다. 
        self.cities_file = cities_file
        self.store_file = store_file
        self.cities2_file = cities2_file
        self.store_num_file = store_num_file
        self.store = []
        self.cities = []
        self.cities2 = []
        self.store_num = []
        

    def generate_store(self, num_people):
        store = self.file_read(self.store_file)
        for _ in range(num_people):
            result_store = random.choice(store)
            self.store.append(result_store)
        return self.store
    
    def generate_cities(self, num_people):
        cities = self.file_read(self.cities_file)
        for _ in range(num_people):
            result_city = random.choice(cities)
            self.cities.append(result_city)
        return self.cities
    
    def generate_cities2(self, num_people):
        cities2 = self.file_read(self.cities2_file)
        for _ in range(num_people):
            result_cities2 = random.choice(cities2)
            self.cities2.append(result_cities2)
        return self.cities2
    
    def generate_store_num(self, num_people):
        store_num = self.file_read(self.store_num_file)
        for _ in range(num_people):
            result_store_num = random.choice(store_num)
            self.store_num.append(result_store_num)
        return self.store_num
    
    def generate_user_data(self, num_people):
        self.generate_store(num_people)
        self.generate_cities(num_people)
        self.generate_cities2(num_people)
        self.generate_store_num(num_people)
        self.save_to_csv_store()

    def save_to_csv_store(self):
        store = []
        
        for i in range(len(self.store)):
            d=random.randint(1, 100)
            people_data = {
                "store_Id": store_Id,
                "상호명" : self.store[i],
                "도시" : self.cities[i],
                "주소" : (f'{self.cities2[i]} {d}로{d}길'),
                "호점" : self.store_num[i]
            }
            store.append(people_data)
        df = pd.DataFrame(store)
        print(df)
        df.to_csv("store.csv", index=False)
Store_generator = StoreDataGenerator("stores.txt","cities.txt","cities2.txt","store_num.txt")

Store_generator.generate_user_data(10)

#getter setter