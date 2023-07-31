import sqlite3
from flask import Blueprint, render_template, request, Flask
from models import Store
from models import Order
from models import Item
from models import OrderItem
from models import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

store_bp = Blueprint('store', __name__)


@store_bp.route('/')
def store():
    page = request.args.get('page', default = 1, type = int)
    per_page = 10
    
    all_stores = Store.query.all()
  

    # 현재 페이지 계산
    current_page = page

    # 현재 페이지 그룹 번호 계산
    current_group = (page - 1) // per_page
      
    #전체 페이지 수를 계산
    total_pages = (len(all_stores) + per_page -1) // per_page
    print(type(all_stores))
    #시작 인덱스와 끝 인덱스를 구해서 페이지를 나눠줘
    start_index = per_page * (page-1)
    end_index = per_page * page
    paginated_results =all_stores[start_index:end_index]

    # 페이지 그룹의 시작 페이지와 종료 페이지 계산
    start_page = current_group * per_page + 1
    end_page = min(start_page + per_page, total_pages)
    
    paginated_results =all_stores[start_index:end_index]
    
    return render_template('store.html', stores = paginated_results
                           ,start_index=start_index,total_pages=total_pages, start_page=start_page
                           ,end_index=end_index,pags=current_page,page=page,end_page=end_page)

    
@store_bp.route('/<id>')
def store_revenues(id):
    store_id = id
    data_format= '%Y-%m'
    revenues = db.session.query(
      db.func.strftime(data_format, Order.orderat).label('Month'),
      db.func.sum(Item.unitprice).label('Revenue'),
      db.func.count(Item.id).label('Count')
    ).join(Store, Store.id == Order.storeid)\
    .join(OrderItem, Order.id == OrderItem.orderid)\
    .join(Item, Item.id==  OrderItem.itemid)\
    .filter(Store.id == store_id)\
    .group_by(Store.name, 'Month')\
    .order_by('Month').all()

    # 매출 정보에서 매출만 따로 추출
    prices = [revenue.Revenue for revenue in revenues]
   
    #TODO 변수로..
    # print(datas)
    print(revenues)
    return render_template("stored_revenues.html", revenues=revenues, prices=prices)

#TODO 자주방문한 매장 top5