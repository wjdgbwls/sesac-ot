import sqlite3
from flask import Blueprint, render_template, request

order_bp=Blueprint('order', __name__)

@order_bp.route('/')
def order():
    


    
    page = request.args.get('page', default = 1 , type = int)
    per_page = 10
    data = []

    conn = sqlite3.connect('./dbfile/user-sample.db')
    cursor = conn.cursor()

    query = "SELECT * FROM orders WHERE 1"
    params = []

    cursor.execute(query, params)
    datas = cursor.fetchall()

    for i in datas:
        data.append(i)
    
    current_page = page
    current_group = (page - 1) // per_page
    total_pages = (len(data) + per_page - 1 ) // per_page
    #시작 인덱스 끝 인덱스
    start_index = per_page * (page-1)
    end_index = per_page * page
    paginated_results = data[start_index:end_index]
    current_group = (page - 1) // per_page
    start_page = current_group * per_page + 1
    end_page = min(start_page + per_page, total_pages)
    
    return render_template("order.html", datas=paginated_results , total_pages=total_pages,
                              page=page, start_page=start_page, end_page=end_page, pags=current_page)