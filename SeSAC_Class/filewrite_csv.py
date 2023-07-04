#csv comma seperated value
import csv

data=[
  ('name','age','city'),
  ('jone',25,'seoul'),
  ('kim',26,'Busan')
]
with open("user.csv", 'r', newline="") as file:
  csv_file = csv.writer(file)
  csv_file.writerows(data)

print('잘 써짐')