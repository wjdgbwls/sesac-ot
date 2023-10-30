#해시를 사용한 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp =""
        for number in phone_number:
            temp += number
            #만약 현재 생성한 접두어가 hash_map에 존재하고, 그 접두어가 현재 검사 중인 전화번호와 같지 않다면 answer를 False로 설정합니다.
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
#문자열 정렬을 사용한 풀이
def solution(phone_book):
    answer = True
    phone_book.sort()  # 전화번호를 사전순으로 정렬
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break
    
    return answer

print(solution(["123","456","789"]))