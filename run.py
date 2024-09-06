import csv
import os
from src.Ingr import Ingr
all_ingr = dict()
db_path = "db"
arr = os.listdir(db_path)
for r in arr:
  f_name = r.split(".")[0]
  f_path = db_path + "/" + r
  with open(f_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      if len(row) > 1:
        id  = row[0].lower()
        qnt = row[1].replace(" ", "")
        unit = ""
        if len(row) > 2:
          unit = row[2].replace(" ", "")
        ingr = Ingr(id, qnt, unit)
        key = ingr.get_key()
        if key in all_ingr.keys():
          all_ingr[key].add(ingr)
        else:
          all_ingr[key] = ingr




for k, i in all_ingr.items():
    #print(i.get_key())
  i.print_info()


   #     print(row)
   #   print(', '.join(row))