m = int(input())

a = list(map(int,input().split()))

n = int(input())
cnt = 0
b = list(map(int,input().split()))

dic={}

for i in b:
    dic[0][i]=0
    print(dic[i])
print(dic)

