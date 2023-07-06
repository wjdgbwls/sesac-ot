import csv

def filepath(path):
    csv_data=[]
    csv_file_path = path
    with open(csv_file_path, 'r', encoding='UTF-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                csv_data.append(row)
            return csv_data