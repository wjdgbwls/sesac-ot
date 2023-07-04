numbers= [3,7,2,9,1,42,23,6,123,23,3223,236]
def find_max(numbers):
  list=[]
  max=numbers[0]
  for i in numbers:
    if max < i:
      max = i
  return max
print("최대값:",find_max(numbers))

def find_max2(text):
  numbers=[]
  strings =text.split()
  for string in strings:
    numbers.append(int(string)) 
  return find_max(numbers)
user_input=input("숫자를 입력하시요(공백으로 구분):")
max_number =find_max2(user_input)
print(find_max2(user_input))

#def find_max3(text):
  #numbers =[int(n) for n in text.split()]
2
  #return find_max(numbers)