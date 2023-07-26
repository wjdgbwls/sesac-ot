from flask import Blueprint, render_template

from models import Item
item_bp = Blueprint('item', __name__)

@item_bp.route('/')
def orderitem():
    data=[]
    all_stores = Item.query.all()
    print(all_stores)
    return render_template("item.html", stores=all_stores)
    