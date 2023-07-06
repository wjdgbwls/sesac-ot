
import filepath
from flask import Blueprint, render_template
import csv

item_bp = Blueprint('item', __name__)

@item_bp.route('/')
def orderitem():

    csv_file_path = "./csvfile/item.csv"
    csv_data = filepath.filepath(csv_file_path)

    return render_template("item.html", itemname = csv_data)