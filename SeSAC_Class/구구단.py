number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    
    rev = rev * 10 + rem
    print(rem,rev)
    number = number // 10

print(rev)