from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  with open(data.csv)