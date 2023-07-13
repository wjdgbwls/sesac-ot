from flask import Flask,render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
  conn = sqlite3.connect('user-sample.db')
  cursor = conn.cursor()
 

  cursor.execute("select * fr")
  tables = cursor.fetchall()
  for table in tables:
    print(table[0])

  return render_template("index.html",row=tables)
if __name__ == "__main__":
  app.run(host="0.0.0.0" , debug=True)