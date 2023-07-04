import random

def generate_us_state_names(num_states):
    us_states = ['Alaska', 'Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Texas', 'New York', 'Kansas']
    
    random_states = random.sample(us_states, num_states)
    
    return random_states

def generate_random_birthdate_gender(num_people):
    # 생년월일 생성을 위한 범위
    start_year = 1950
    end_year = 2005

    # 성별 리스트
    genders = ['남성', '여성']

    people = []
    
    for _ in range(num_people):
        # 생년월일 생성
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # 단순화를 위해 모든 달을 28일로 가정합니다.

        # 성별 선택
        gender = random.choice(genders)

        # 개인 정보 추가
        person_info = {
            '생년월일': f'{year}년 {month}월 {day}일',
            '성별': gender
        }

        people.append(person_info)
    
    return people

def main():
    # 미국 주 이름 생성 함수 호출
    random_states = generate_us_state_names(10)

    # 개인 정보 생성 함수 호출
    random_people = generate_random_birthdate_gender(10)

    data = []
    for i in range(10):
        person = {
            '주': random_states[i],
            '생년월일': random_people[i]['생년월일'],
            '성별': random_people[i]['성별']
        }
        data.append(person)

    # 결과 출력
    for person in data:
        print(f'주: {person["주"]}, 생년월일: {person["생년월일"]}, 성별: {person["성별"]}')
    print(data)

# 메인 함수 실행
main()