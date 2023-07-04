
def korean_number(c):
    lists=['영','일','이','삼','사','오','육','칠',]
    
    for list in lists:
        str=""
        if c == list:
            str += list
    return str
print(korean_number(1))