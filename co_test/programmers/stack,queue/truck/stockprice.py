def solution(prices):
    answer = [0] * len(prices)
    #prices의 
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

###################################
#deque를 이용한 풀이
from collections import deque
def solution(prices):
    answer = []
    #deque를 사용하는 방법
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
#deque는 앞뒤로 사용할 수 있음 큐와 스택을 합쳐놓은 