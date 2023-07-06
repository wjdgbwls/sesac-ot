import filepath
from flask import Blueprint, render_template
import csv

store_bp = Blueprint('store', __name__)

@store_bp.route('/')
def store():
    csv_file_path = "./csvfile/store.csv"
    csv_data = filepath.filepath(csv_file_path)
    print(csv_data)
    return render_template("store.html", storename = csv_data)