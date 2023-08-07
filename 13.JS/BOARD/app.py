from flask import Flask,render_template, request, jsonify
from database import Database
import sqlite3

app = Flask(__name__)
db = Database()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods =['post'])
def create():
    title = request.form['title']
    message = request.form['message']
    print(title,message)
    sql = "insert into board(title,message) values ('{}','{}')".format(title,message)
    db.execute(sql)
    db.commit()
    return ""

@app.route('/list', methods = ['get'])
def list():
    db = Database()
    sql = "SELECT * FROM board"
    result = db.execute_fetch(sql)
    
    # 조회 결과를 JSON 형태로 변환하여 반환
    columns = [column[0] for column in db.cursor.description]
    data = [dict(zip(columns, row)) for row in result]
    posts =data
    print(posts)
    return posts
@app.route('')
# def update():
#     db = Database()
#     sql = "UPDATE ??? FROM board >>>"
#     data
#     return data
@app.route('')
def delete():
    return 
if __name__=='__main__':
    app.run(debug=True)
