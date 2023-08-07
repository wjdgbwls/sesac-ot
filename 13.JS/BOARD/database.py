import sqlite3

class Database():
    def __init__(self):
        self.db = sqlite3.connect('board.sqlite', check_same_thread=False)
        self.cursor = self.db.cursor()  # 커서 생성
    # 커서 생성
    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def execute_fetch(self, query, args ={}):
        self.cursor.execute(query, args)
        result = self.cursor.fetchall()
        return result
    
    def commit(self):
        self.db.commit()     

if __name__ == '__main__':
    db = Database()# 데이터 추가
    db.execute("INSERT INTO board(title,massage) VALUES (?,?)",('hello','world'))
    db.commit()