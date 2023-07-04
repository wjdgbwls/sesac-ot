#사용자로부터 입력을 받음
#연산모드를 입력받는다 곱셈 나눗셈 
#숫자 두 개
#결과를 보여준다
#시랳ㅇ 에씨
#연산모드를 입력하시오:plus /minus / multiply / division
class Calculater:
  
    def input_mode(self):
        #while문을 넣어서 밑에 재귀를 사용하지 않고 돌아가게 변경하기
        mode=input("모드를 입력하세요: ")
        modes=['plus','minus','div','mul']
        if mode in modes:
          return mode
        else:
          print("다시 입력해 주쇼: ")
          mode = self.input_mode() #class로 변경시 self를 사용해야됌
        
          
    def input_val1():
        try:
          val1= int(input("숫자1을 입력하시오: "))
        except ValueError:
          print("입력이 정확하지않음")
          print("다시 :")
          val1 = input_val1()
        return val1
    def input_val2():
        try:
          val2= int(input("숫자1을 입력하시오: "))
        except ValueError:
          print("입력이 정확하지않음")
          print("다시 :")
          val2 = input_val2()
        return val2


    def calc(mode,val1,val2):
        if mode == 'plus':
              return val1+val2
        elif mode == 'minus':
            return val1-val2
        elif mode == 'mul':
            return val1*val2
        elif mode == 'div':
            try:
              div1=round(val1+val2)
              return (div1)
            except ZeroDivisionError:
              print("ZeroDivisionError!!")
        else:
          print('알수없는 숫자입니다')
        
    mode= input_mode()
    val1=input_val1()
    val2=input_val2()
    print(calc(mode,val1,val2))
    '''def plus(a,b):
        return a+b
    print(plus(a,b))

    def minus(a,b):
        return a-b
    def multiply(a,b):
        return(a*b)
    def division(a,b):
        if a == 0 or b == 0:
            print("0을 넣어서 프로그램이 종료됌")
        else:
            return(a/b)'''
    if __name__ == "__main__":
      while True:
        v=input("연산을 종료하시려면 x를 입력하세요: ")
        if v == 'x':
          break
        else:
          mode = input_mode()
          val1 = input_val1()
          val2 = input_val2()
          print(calc(mode,val1,val2))

      #일반적으로는 함수에는 return을 한번만 사용한다 꼭 그래야만 하는 거슨 아니다