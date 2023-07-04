def remove_duplicate(lists):
    print(lists)
    unique_list=[]
    for list in lists:
      if list not in unique_list:
         unique_list.append(list)
    return unique_list

user_input=list(map(int, input("숫자를 입력 해 : ").split()))

print(remove_duplicate(user_input))