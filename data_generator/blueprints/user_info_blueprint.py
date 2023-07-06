from flask import Blueprint, render_template
import filepath
import csv

# 블루프린트 객체는 Blueprint 클래스의 인스턴스로
# 'user'라는 이름과 __name__을 인자로 전달하여 생성됩니다.
#블루프린트를 생성하는 객체
user_info_bp = Blueprint('user_info', __name__) 

@user_info_bp.route('/<Id>')
def user(Id):
    data=[]
    csv_reader=filepath.filepath("./csvfile/user.csv")
    for user in csv_reader:  
        if user['Id'] == Id:
            data = user
            break
    return render_template("index_user_info.html", user=data)