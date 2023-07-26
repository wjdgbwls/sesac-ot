from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    #테이블 이름 지정(옵셔널)
    __tablename__ = 'users'
    # 컬럼 셋업
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    age = db.Column(db.Integer())
    birthdate = db.Column(db.String(32))
    address = db.Column(db.String(64))
    #rhksrP 
    orderR = db.relationship('Order', backref='users')

class Store(db.Model):
     __tablename__ = 'stores'
     id = db.Column(db.String(64),primary_key=True)
     name = db.Column(db.String(32))
     type = db.Column(db.String(32))
     address = db.Column(db.String(64))
     orderR = db.relationship('Order', backref='stores')
class Order(db.Model):
     __tablename__ = 'orders'
     id = db.Column(db.String(64),primary_key=True)
     orderat = db.Column(db.String(64))
     storeid = db.Column(db.String(64), db.ForeignKey('stores.id'))
     userid = db.Column(db.String(64), db.ForeignKey('users.id'))
class Item(db.Model):
     __tablename__ = 'items'
     id = db.Column(db.String(64),primary_key=True)
     name = db.Column(db.String(64))
     type = db.Column(db.String(64), db.ForeignKey('stores.id'))
     unitprice = db.Column(db.String(64), db.ForeignKey('users.id'))

