'''number=[1,2,3,4,5]

value = number[1]

def get_number(index):
    try:
      # 오류 발생 가능성이 있는 코드 블럭
      return number[index]
    except IndexError:
       #오류에 대한 처리 방법
       print('인덱스 번호가 잘못됌')
    except TypeError:
       print('데이터 입력값의 유형이 잘못됌')
print(get_number(0))

print(get_number(5))

print(get_number(2))

print(get_number('a'))'''

# 글자를 입력받아 숫자로 변환하세요
# 사용자를 입력받아  
def convert_to_integer(str):
  value = None
  try:
    value = int(str)
  except ValueError:
    print("변환 할 수 없는 입력값입니다")
  return value
print(convert_to_integer("10"))
print(convert_to_integer("-5"))
print(convert_to_integer("-5"))
print(convert_to_integer("A"))
print(convert_to_integer("Hello"))