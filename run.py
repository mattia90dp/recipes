import csv
import os
db_path = "db"
arr = os.listdir(db_path)
for r in arr:
  f_name = r.split(".")[0]
  f_path = db_path + "/" + r
  with open(f_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    print(f_name)
    for row in spamreader:
      print(', '.join(row))