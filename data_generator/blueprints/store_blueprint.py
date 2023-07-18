import sqlite3
from flask import Blueprint, render_template, request
import csv

store_bp = Blueprint('store', __name__)

@store_bp.route('/')
def store():
    page = request.args.get('page', default = 1, type = int)
    per_page = 10
    data=[]
      # SQLite 데이터베이스 연결
    conn = sqlite3.connect('./dbfile/user-sample.db')
    cursor = conn.cursor()
    
    # SQL 쿼리 작성
    query = "SELECT * FROM stores WHERE 1"
    # 결과 가져오기
    cursor.execute(query)
    datas = cursor.fetchall()
    for i in datas:
        data.append(i)

      # 현재 페이지 계산
    current_page = page

      # 현재 페이지 그룹 번호 계산
    current_group = (page - 1) // per_page
      
      #전체 페이지 수를 계산
    total_pages = (len(data) + per_page -1) // per_page

      #시작 인덱스와 끝 인덱스를 구해서 페이지를 나눠줘
    start_index = per_page * (page-1)
    end_index = per_page * page
    paginated_results =data[start_index:end_index]
    

      # 현재 페이지 그룹 번호 계산
    current_group = (page - 1) // per_page

      # 페이지 그룹의 시작 페이지와 종료 페이지 계산
    start_page = current_group * per_page + 1
    end_page = min(start_page + per_page, total_pages)
    
    paginated_results =data[start_index:end_index]
    return render_template("store.html",datas=paginated_results,total_pages=total_pages,page=page ,
                           start_page=start_page, 
                           end_page=end_page, pags=current_page)