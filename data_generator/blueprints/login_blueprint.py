import sqlite3

from flask import Blueprint, render_template


login_bp = Blueprint('login', __name__)

@login_bp.route('/')
def login():
    data=[]
    conn = sqlite3.connect('./dbfile/user-sample.db')
    cursor = conn.cursor()
    datas = cursor.fetchall()
    # SQL 쿼리 작성
    query = "SELECT * FROM items WHERE 1"
    cursor.execute(query)
    datas = cursor.fetchall()
    for i in datas:
        data.append(i)
    return render_template("item.html", itemname = data)

#redirect는 실행하는 함수를 불러온다 login()같은 함수