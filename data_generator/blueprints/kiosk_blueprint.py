import sqlite3
from flask import Blueprint, render_template

kiosk_bp = Blueprint('kiosk', __name__)

@kiosk_bp.route('/')
def store_list():
    data=[]
    conn = sqlite3.connect('./dbfile/user-sample.db')
    cursor = conn.cursor()
  
    # SQL 쿼리 작성
    query = "SELECT * FROM stores"
    cursor.execute(query)
    datas = cursor.fetchall()
    for i in datas:
        data.append(i)
    return render_template("kiosk.html", datas = data)

@kiosk_bp.route('/<id>')
def store_select(id):
    id = (id,)
    data=[]
    conn = sqlite3.connect('./dbfile/user-sample.db')
    cursor = conn.cursor()
    query = """select distinct items.Name, items.UnitPrice form             
                            FROM stores
                            INNER JOIN orders ON stores.Id = orders.StoreId 
                            INNER JOIN order_items ON orders.Id = order_items.OrderId 
                            INNER JOIN items ON order_items.ItemId = items.Id WHERE stores.Id = ?"""
    cursor.execute(query,id)
    datas = cursor.fetchall()
    for i in datas:
        data.append(i)
    return render_template("kiosk_items.html", datas = data)