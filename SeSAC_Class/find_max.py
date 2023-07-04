'''def find_max(text):
    max=text[0]
    for c in text:
        if max < c:
            max = c
    return max

num = list(map(int, input('숫자를 입력해 : ').split()))
print(find_max(num))'''
sum=0
while True:
    num = int(input())
    if num < 0:
        break
    else:
        sum += num
print(sum)
