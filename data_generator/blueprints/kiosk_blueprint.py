import sqlite3
from flask import Blueprint, render_template

kiosk_bp = Blueprint('kiosk', __name__)

@kiosk_bp.route('/')
def orderitem():
    data=[]
    conn = sqlite3.connect('./dbfile/user-sample.db')
    cursor = conn.cursor()
  
    # SQL 쿼리 작성
    query = "SELECT * FROM stores WHERE 1"
    cursor.execute(query)
    datas = cursor.fetchall()
    for i in datas:
        data.append(i)
    return render_template("kiosk.html", datas = data)