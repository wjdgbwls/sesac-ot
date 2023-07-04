from flask import Flask, url_for, redirect

app = Flask(__name__) #자동으로 사용되는 모듈네임 같은거

@app.route('/')
def main():
    return """
    <HTML>
    <HEAD>
    <TITLE>마이타이틀</TITLE>
    <BODY>
    <H1>hello sesac from flask</H1>
    <a href= "/user">welcome to  Flask Class</a>
    </BODY>
    </HEAD>
    <HTML>
    
"""
@app.route('/user')
def user_none():
    return"""
    <UL>
    <LI> <a href="/user/tom">tom</a> </LI>
    <LI> <a href="/user/jone">jone</a> </LI>
    <LI> <a href="/user/bill">bill</a> </LI>
    </UL>
    """

@app.route('/user/<name>')
def user(name):
    return f"""
    <H1>This is {name}'s Homepage</H1><a href="/">go back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)

app.route('/admin')

def admin():
    return redirect(url_for('user', name="admin")) #user라는 메소드를 호출하고 admin이라는 이름을 보냄