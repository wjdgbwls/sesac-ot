import json
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__)
app.secret_key = "yoser_skjdf"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sessions.db'
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] ='sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
Session(app)
class SessionData(db.Model):
    id = db.Column(db.String(255), primary_key =True)
    data = db.Column(db.Text)

def session_store(sid, data):
    session_data = SessionData.query.get(sid)
    if not session_data:
        session_data = SessionData(id = sid)
    
    session_data.data = json.dumps(data)
    db.session.add(session_data)
    db.session.commit()
@app.route('/')
def index():
    session['username'] = 'user'
    session['data'] = '1234'

    # 숫자 데이터 저장
    session['count'] =42

    session['my_list']=[1,2,3,4,5]

    session_store(session.sid, dict(session))
    return 'hello'
def get_session_data(sid):
    session_data = SessionData.query.get(sid)
    if session_data:
        return json.loads(session_data.data)
    return {}

@app.route('/get_session')
def get_session_data_route():
    username = session.get('username')
    data = session.get('data')

    #저장된 데이터 불러오기
    stored_session_data = get_session_data(session.id)
    print(stored_session_data)
    stored_session_str = json.dumps(stored_session_data, intent=4)

    return f'username :{username}, {data}, my-data :{stored_session_str}'

if __name__ == "__main__":
    with app.app_context():# db를 만들었으니 디비를 초기화해야됌
      db.create_all()
    app.run(debug=True)