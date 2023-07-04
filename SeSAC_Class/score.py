'''while True:
    max=None
    h='high'
    v=input("종료하려면 x를 누르세요: ")
    if v == 'x':
        break
    else:
        list_score=[]
        list_man=[]
        a=int(input("점수를 입력하세요: "))
        list_score.append(a)
        b=input("사람을 입력하세요: ")  
        list_man.append(b)
        for man in list_man:
            for score in list_score:
              if max < int(score):
                  max = score
                  print('high',man)
        his=input("history입력하면 점수와 사람을 확인할 수 있음: ")
        if his == 'history':
            print(list_score,list_man)'''
class Calculater:
    game_highscore=0 
    game_history=[]
    def input_score(self):
        score= int(input("점수: "))
        name = input("이름: ")

        return score, name
    def print_history():
        print('-------------------------')
        print('점수, 이름')
        print('-------------------------')
        print(game_history)

    def store_result(score,name)
        while True:
            game_score=(score,name)
            game_history.append(game_score)
    def high_score(high_score):
        
        for score, _ in game_highscore:
            if high_score < score:
                high_score = score
                print("최고점수: ", high_score)       
            print(score[0]) #10, 20
    def main():
        while True:
            op = input_mode() # 모드를 입력하고
            if op == 'score':
              # 스코어와 이름을 입력함
              score,name = input_score()
            #elif op == 'high':
                
    def input_mode():
        mode_ops=['score','high','history']
        mode= input("입력모드 : ")
        if mode not in mode_ops:
          mode= input("입력모드 : ")
        return mode

    #미션 2 history라고 입력하면 점수와 사람
