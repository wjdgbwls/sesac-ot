
from flask import Flask, render_template, request
import csv

app = Flask(__name__)
# sample_str = sample_str.replace(' ','')
# csv_data = csv.DictReader(파일이름)
# headers = [header.strip() for header in csv_data.fieldnames]

# clean_row = {key.strip(): value.strip() for key, value in row.item()}
# return render_template('index.html' headers=header, data =data)
@app.route('/')
def page_index():
    page = request.args.get('page', default =1, type=int)
    search_name = request.args.get('q', default='', type =str)
    gender = request.args.get('gender', default='', type =str)
    data=[]
    
    per_page = 10
    csv_file_path = "./csvfile/user.csv"
    with open(csv_file_path, 'r', encoding='UTF-8') as file:
      csv_data = csv.DictReader(file)
      # 검색어를 포함하는 결과 필터링
      for row in csv_data:
        if search_name in row['Name'] and gender == row['Gender']:
          data.append(row)
        elif gender == '':
          data.append(row)
            
        
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
                              page=page, search_name=search_name, start_page=start_page, end_page=end_page, pags=current_page, gender = gender)

              
# @app.route('/<name>')
# def userinfo(name=""):
    
#     csv_file_path = "csvfile/user.csv"
#     with open(csv_file_path, 'r', encoding='UTF-8') as file:
#       csv_reader = csv.reader(file)
#       return render_template("index.html", username=csv_reader)
    # 2.num에 갯수만큼 데이터를 잘라준다
    # 3.페이지에 이 데이터를 전달한다.
    # 4.페이지를 구분하기 위한 인덱스
    # 5. 인덱스의 시작부터 끝까지 숫자를 전달한다.
#=================================
#유저의 정보를 가져온다..
#=================================
@app.route('/user/<Id>')
def user(Id):
    data=[]
    csv_file_path = "./csvfile/user.csv"
    with open(csv_file_path, 'r', encoding='UTF-8') as file:
      csv_reader = csv.DictReader(file)
      for user in csv_reader:
        if user['Id'] == Id:
            data = user
            break
      return render_template("index_user_info.html", user=data)
#=================================
#store의 정보를 가져온다..
#=================================
@app.route('/store')
def store():
    csv_file_path= "./csvfile/store.csv"
    with open(csv_file_path, 'r', encoding="UTF-8") as file:
      csv_reader = csv.reader(file)
      return render_template("store.html", storename =csv_reader)
#=================================
#item의 정보를 가져온다..
#=================================    
@app.route('/item')
def item():
    csv_file_path= "./csvfile/item.csv"
    with open(csv_file_path, 'r', encoding="UTF-8") as file:
      csv_reader = csv.reader(file)
      return render_template("item.html", itemname = csv_reader)
#=================================
#order의 정보를 가져온다..
#=================================
@app.route('/order')
def order():
    csv_file_path= "./csvfile/order.csv"
    with open(csv_file_path, 'r', encoding="UTF-8") as file:
      csv_reader = csv.reader(file)
      return render_template("order.html", ordername = csv_reader)
#=================================
#orderitem의 정보를 가져온다..
#=================================
@app.route('/orderitem')
def orderitem():
    csv_file_path= "./csvfile/order.csv"
    with open(csv_file_path, 'r', encoding="UTF-8") as file:
      csv_reader = csv.reader(file)
      return render_template("orderitem.html", orderitemname = csv_reader)
#=================================
# hello2.py를 실행한다 
#=================================
if __name__ == "__main__":
  app.run(host="0.0.0.0" , debug=True)
#미션1 사용자 이름을 우리의 csv파일로 대체