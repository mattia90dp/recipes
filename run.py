import csv
import os
import random

from src.Ingr import Ingr

all_ingr = dict()
db_path = "db"
arr = os.listdir(db_path)

all_r = []

for r in arr:
  f_name = r.split(".")[0]
  all_r.append(f_name)
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
  i.print_info()

class DailyPlan:
  def __init__(self, day, l, d):
    self.day = day
    self.l = l
    self.d = d
  def print_info(self):
    template = "{0:5} {1:8} {2:10}"
    dbg = template.format(k, "Lunch  :", str(self.l))
    print(dbg)
    dbg = template.format(k, "Dinner :", str(self.d))
    print(dbg)

week_d = dict()
week_d["Mon"] = DailyPlan("Mon", 0, 0)
week_d["Tue"] = DailyPlan("Tue", 0, 0)
week_d["Wed"] = DailyPlan("Wed", 0, 0)
week_d["Th"]  = DailyPlan("Th" , 0, 0)
week_d["Fr"]  = DailyPlan("Fr" , 0, 0)
week_d["Sat"] = DailyPlan("Sat", 0, 0)
week_d["Sun"] = DailyPlan("Sun", 0, 0)


prev_d = random.randrange(0, len(all_r))
for k, i in week_d.items():
  l = prev_d
  d = prev_d
  template = "{0:5} {1:8} {2:10}"

  while l == d:
    l = prev_d
    d = random.randrange(0, len(all_r))
    prev_d = d
  i.l = all_r[l]
  i.d = all_r[d]
  i.print_info()