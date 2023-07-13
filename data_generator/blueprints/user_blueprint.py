import filepath
import sqlite3
from flask import Blueprint,render_template, request
import csv

user_bp=Blueprint('user',__name__)

@user_bp.route('/')
def user():
    page = request.args.get('page', default =1, type=int)
    search_name = request.args.get('q', default='', type =str)
    gender = request.args.get('gender', default='', type =str)
    per_page = 10
    data=[]
     # SQLite 데이터베이스 연결
    conn = sqlite3.connect('./dbfile/user-sample.db')
    cursor = conn.cursor()
    
    # SQL 쿼리 작성
    query = "SELECT * FROM users WHERE 1"
    params = []

    # 검색어 필터링
    if search_name:
        query += " AND Name LIKE ?"
        params.append(f"%{search_name}%")

    # 성별 필터링
    if gender:
        query += " AND Gender = ?"
        params.append(gender)

    # 결과 가져오기
    cursor.execute(query, params)
    datas = cursor.fetchall()
        
    for i in datas:
        data.append(i)
    #      ##############여기 gender를 확인하고 그걸 추가하는 줄 하나 ....넣기
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
      
    return render_template("home.html", datas=paginated_results , total_pages=total_pages,
                              page=page, search_name=search_name, start_page=start_page, end_page=end_page, pags=current_page)


#
#csv
#
  # 
    # #header_data=[]
    # 
    # csv_file_path = "../csvfile/user.csv"
    # with open(csv_file_path, 'r', encoding='UTF-8') as file:
    #   csv_data = csv.DictReader(file)
    #   #header_data=csv_data[0]
    #   # 검색어를 포함하는 결과 필터링
    #   for row in csv_data:
    #     if search_name in row['Name'] and gender == row['Gender']:
    #       data.append(row)
    #     elif gender == '':
    #       data.append(row)