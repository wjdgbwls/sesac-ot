import random


class AddressGenerator():
    def __init__(self):
        self.cities = ['서울', '부산', '대구', '인천', '광주']
        self.gus = ['강남구', '강서구', '중구', '남구', '서구']
        self.streets = ['길', '로']

    def generate(self, num_people):
        address=[]
        city = random.choice(self.cities)
        gu = random.choice(self.gus)
        street = random.choice(self.streets)
        for i in range(num_people):
          road_number = random.randint(1, 100)
          road_number2 = random.randint(1, 100)
          address = f"{city} {gu} {road_number}{street} {road_number2}"
        return self.address 