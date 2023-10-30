# def solution(participant, completion):
#     result = {}
#     for a in participant:
#         result[a] = result.get(a, 0) + 1
#     print('++++',result)
#     for b in completion:
#         result[b] -= 1
#         if result[b] == 0:
#             del result[b]
#     return list(result.keys())[0]
###########################################################
###########################################################
###########################################################
# def solution(participant, completion):
#     participant_hash = {}
    
#     for person in participant:
#         if person in participant_hash:
#             participant_hash[person] += 1
#         else:
#             participant_hash[person] = 1
    
#     for person in completion:
#         if person in participant_hash:
#             participant_hash[person] -= 1
#             if participant_hash[person] == 0:
#                 del participant_hash[person]
    
#     for key in participant_hash:
#         return key
###########################################################
###########################################################
def solution(participant, completion):
    participant_hash = {}
    
    for person in participant:
        participant_hash[person] = participant_hash.get(person, 0) + 1
    
    for person in completion:
        participant_hash[person] -= 1
    
    for key, value in participant_hash.items():
        if value > 0:
            return key
###########################################################
###########################################################
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        #해시값을 할당함
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
