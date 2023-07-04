users=[
    {"name":"alice","age":25 ,"location":"Seoul","car":"BMW"},
    {"name":"Bob","age":30 ,"location":"Busan","car":"meres"},
    {"name":"charile","age":35 ,"location":"Daegu","car":"Audi"},
]

search_user={
  "name":"Bob",
  "age":30,
  "location":"Busan"
  }
def find_users(search_user):
    result = []
    for user in users:
        match = True
        for key, value in search_user.items():
            if key in user and user[key] != value:
                match = False
                break
        if match:
            result.append(user)
    return result
result = find_users(search_user)
print(result)
'''def matches_criteria(user,condition)
    return 

def find_users(search_user):
    result=[]
    for user in users:
        if matches_criteria(user, search_user):
            result.append(user)
    return result'''
search_bob1 ={"name":"Bob"}
search_bob2 ={"age": 30}
search_bob3={"name": "Bob", "age": 30}
search_bob4={"name": "Bob", "age": 31}
search_bob5={}

test_cases=[{"case": search_bob1,"expect_result":1},
            {"case": search_bob2,"expect_result":1},
            {"case": search_bob3,"expect_result":1},
            {"case": search_bob4,"expect_result":0},
            {"case": search_bob5,"expect_result":3}
            ]
#test_results =[1,1,1,0,3]


def test_find_user():
    for test_case in test_cases:
        if not len(find_users(test_case)) == test_cases['expect_result']:
            final_result = False
    '''for i,test_case in enumerate(test_cases):
        if len(find_users(test_case)) == test_results[i]:'''  
        
    '''if not len(find_users(search_bob1)) == 1:
        final_result = False
    if not len(find_users(search_bob2)) == 1:
        final_result =  False 
    if not len(find_users(search_bob3)) == 1:
        final_result= False
    if not len(find_users(search_bob4)) == 0:
        final_result= False
    if not len(find_users(search_bob5)) == 3:
        final_result= False
    
    if final_result is True:
        print('PASS')
    else:
        print('False')
    return'''

test_find_user()


