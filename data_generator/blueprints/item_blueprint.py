import sqlite3
import filepath
from flask import Blueprint, render_template
import csv

item_bp = Blueprint('item', __name__)

@item_bp.route('/')
def orderitem():
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