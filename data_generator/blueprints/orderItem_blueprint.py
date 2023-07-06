import filepath
from flask import Blueprint, render_template
import csv

orderItem_bp = Blueprint('orderitem', __name__)

@orderItem_bp.route('/')
def orderitem():
    csv_file_path = "./csvfile/orderitem.csv"
    csv_data = filepath(csv_file_path)
    return render_template("orderitem.html", orderitemname = csv_data)