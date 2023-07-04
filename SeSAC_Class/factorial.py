##a=int(input())
#num =1
#for i in range(1,a+1):
 #  num *=i #ex 5면 1*2*3*4*5
#print(num)
def fac(n):
   if(n>1):
      return n * fac(n-1)
   else:
      return 1
n=5
print("fac:",fac(n))
#-----------피보나치
def fib(n):
   if n <= 1:
      return n
   return fib(n-1)+fib(n-2)
n=8
print("fib:",fib(n))