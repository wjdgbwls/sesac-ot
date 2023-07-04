num =int(input())
result = str(num)

if num > 1000000:
    result = str(num // 100000) +'m'
elif num  >= 0:
    pass
print(result)
print("안녕하세요")