import datetime
#각 모듈별 사용법은?? 원작자들이 메뉴얼을 만들어 둠
#NOT TO DO : 네이버 블로그 남의 글 참조하지 않기
#TO DO: 원문을 참조해야됌

# https://docs.pyhon.org
current_time=datetime.datetime.now()
            #모듈명.클래스명.함수명

print("현재시간:" , current_time)

specific_time = datetime.datetime(2023, 6 ,20 ,10 ,30 ,00)
print("내가만든 날짜: " ,specific_time)
