import sqlite3
from flask import Blueprint, render_template
import filepath
import csv

# 블루프린트 객체는 Blueprint 클래스의 인스턴스로
# 'user'라는 이름과 __name__을 인자로 전달하여 생성됩니다.
#블루프린트를 생성하는 객체
user_info_bp = Blueprint('user_info', __name__) 

@user_info_bp.route('/<id>')
def user(id):
    id = (id,)
    data=[]
    conn=sqlite3.connect('./dbfile/user-sample.db')
    cursor=conn.cursor()
    query='select * from users where Id =?'
    cursor.execute(query, id)
    
    result= cursor.fetchall()
    print(result)
    return render_template("index_user_info.html", user=result)