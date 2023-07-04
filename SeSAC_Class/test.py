# 튜플(a,b)
def get_name():
  return "Jone", 25

if __name__ == "__main__": #개별 노드별로 쓸꺼냐
  name, age = get_name()
  print(name,age)

# 리스트
shopping_list =["apple","banana","orange"]
print(shopping_list)
shopping_list.append("grape")
print(shopping_list)
shopping_list.remove("banana")
print(shopping_list)

#딕셔너리(dictionary)
#Key_Value"이름":"정휴진"
student = {
  "name":"jone",
  "age":20,
  "uni":"Abc uni"
}
print("name", student["name"])
print("age", student["age"])

#---------------------
numbers =[1,2,3,4,5]
#for num in numbers:
  #if num % 2 == 0:
   # print(num, "is 짝수")
  #else:
   # print(num, "is 홀수")
  # 홀수 리스트와 짝수리스트를 따로 만들어서 목록에 추가

  #even_numbers 라는 리스토아 ,odd_numbers 라는 리스트
even_numbers=[]
odd_numbers=[]
for num in numbers:
  if num % 2 == 0:
    even_numbers.append(num)
  else:
    odd_numbers.append(num)  
print(even_numbers,odd_numbers)

student_grade= {
  "jone":"90",
  "emily":20,
  "mic":90,
  "sho":90,
}
#이 목록에서 90점 이상인 학생을 출력하시오

for student, grade in student_grade.item():
  if grade >90:
    print(student)

def nested_loop():
  n = 10
  count=0
  for i in range(n):
    for j in range(n):
      for k in range(n):
        for l in range(n):
          count += 1
  return count
result = nested_loop
print(result)