
class Ingr:
  def __init__(self, id, qnt, unit = None):
    self.id   = id
    self.qnt  = int(qnt)
    self.unit = unit.replace(" ","")
  def get_key(self):
    return(self.id)
  def add(self, another):
    self.check_same_unit(another)
    self.qnt = self.qnt + another.qnt
  def sub(self, another):
    self.check_same_unit(another)
    self.qnt = self.qnt - another.qnt
  def check_same_unit(self, another):
    try:
      self.unit == another.unit
    except Exception:
      print("Unit is not the same")
  def print_info(self):
    template = "{0:20} {1:20} {2:20}"
    print(template.format(self.id, self.qnt, self.unit))
