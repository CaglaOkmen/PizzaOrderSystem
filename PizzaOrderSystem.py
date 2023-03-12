import csv
import datetime

def main():
  Menu()
  menu_text = open("menu.txt", "r")
  oku = menu_text.read()
  print(oku)
  pizz = input("seçilen pizza: ")
  list = ["Classic","Margherita","TurkPizza","PlainPizza"]
  list2 = ["Zeytin","Mantar","Peynir","Et","Sogan","Misir"]
  if pizz in list:
    price = 0
    Class_list = [Classic(None,None),Margherita(None,None),TurkPizza(None,None),PlainPizza(None,None)]
    for i in range(4):
      if list[i] == pizz :
        price = Class_list[i].get_cost()
        name = Class_list[i].get_description()
        Pizza(name, price).get_cost()
        Pizza(name,price).get_description()

  ext = input("secilen extra: ")
  if ext in list2:
    price2 = 0
    Extra_list = [Zeytin(None,None),Mantar(None,None),Peynir(None,None),
                  Et(None,None),Sogan(None,None),Misir(None,None)]
    for i in range(6):
      if list2[i] == ext:
        price2 = Extra_list[i].get_cost()
        name2 = Extra_list[i].get_description()
        Decorator(name2,price2).get_cost()
        Decorator(name2,price2).get_description()
  dict["total"] = dict["pizza_cost"] + dict["extra_cost"]
  
  while(True):
    try:
      isim = input("isim: ")
      int(isim)
      print("Lütfen tekrar giriniz.")
    except ValueError:
      break

  while(True):
    try:
      soyisim = input("soyisim: ")
      int(soyisim)
      print("Lütfen tekrar giriniz.")
    except ValueError:
      break
    
  while(True):
    try:
      tc= int(input("tc: "))
      break
    except ValueError:
        print("Lütfen tekrar giriniz.")

  while(True):
    try:
      kartno = int(input("kredi kart no: "))
      break
    except ValueError:
      print("Lütfen tekrar giriniz.")

  parola= input("şifre: ")
  Person(isim,soyisim,tc,kartno,parola).users_information()

dict = {"pizza_name":"","pizza_cost":0,"extra_name":"","extra_cost":0,"total":0}
class Pizza:
  def __init__(self,name,cost):
    self.name = name
    self.cost = cost

  def get_description(self):
    dict["pizza_name"] = self.name
    print(self.name)
  def get_cost(self):
    dict["pizza_cost"] = self.cost
    print(self.cost)
    
class Classic(Pizza):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_description(self):
    return "Classic: domates, mozzarella, feslegen"
  def get_cost(self):
    return 25

class Margherita(Pizza):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_description(self):
    return "Margherita: mozzarella, pizza sos"
  def get_cost(self):
    return 20

class TurkPizza(Pizza):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_description(self):
    return "TurkPizza: kiyma, sogan, biber, salca"
  def get_cost(self):
    return 35

class PlainPizza(Pizza):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_description(self):
    return "PlainPizza: mozzarella, parmesan, provolone"
  def get_cost(self):
    return 30

class Decorator:
  def __init__(self,name,cost):
    self.name=name
    self.cost=cost

  def get_cost(self):
    dict["extra_cost"] = self.cost
    print(self.cost)
  def get_description(self):
    dict["extra_name"] = self.name
    print(self.name)

class Zeytin(Decorator):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_cost(self):
    return 3
  def get_description(self):
    return "Zeytin"
  
class Mantar(Decorator):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_cost(self):
    return 5
  def get_description(self):
    return "Mantar"

class Peynir(Decorator):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_cost(self):
    return 7
  def get_description(self):
    return "Peynir"

class Et(Decorator):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_cost(self):
    return 9
  def get_description(self):
    return "Et"

class Sogan(Decorator):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_cost(self):
    return 5
  def get_description(self):
    return "Sogan"

class Misir(Decorator):
  def __init__(self, name, cost):
    super().__init__(name, cost)

  def get_cost(self):
    return 3
  def get_description(self):
    return "Misir"

def Menu():
  menu_text = open("menu.txt", "w")
  menu_text.write("Lutfen bir pizza seciniz:\n")
  menu_text.write("1: Classic(25TL)\n")
  menu_text.write("  Icindekiler: domates, mozzarella, feslegen\n")
  menu_text.write("2: Margherita(20TL)\n")
  menu_text.write("  Icindekiler: mozzarella, pizza sos\n")
  menu_text.write("3: TurkPizza(35TL)\n")
  menu_text.write("  Icindekiler: kiyma, sogan, biber, salca\n")
  menu_text.write("4: PlainPizza(30TL)\n")
  menu_text.write("  Icindekiler: mozzarella, parmesan, provolone\n")
  menu_text.write("Ekstra malzeme seciniz:\n")
  menu_text.write(" 1: Zeytin(3TL)\n")
  menu_text.write(" 2: Mantar(5TL)\n")
  menu_text.write(" 3: Peynir(7TL)\n")
  menu_text.write(" 4: Et(9TL)\n")
  menu_text.write(" 5: Sogan(5TL\n")
  menu_text.write(" 6: Misir(3TL)\n")
  menu_text.write("Tesekkurler!")
  menu_text.close()

class Person():
  def __init__(self,FirstName,LastName,Tc,card,parola):
    self.FirstName = FirstName
    self.LastName = LastName
    self.Tc = Tc
    self.card = card
    self.parola = parola

  def users_information(self):
    try:
        with open("Orders_Database.csv", mode="a", newline="") as f:
          write = csv.writer(f, delimiter="-")
          write.writerow(["Kullanici Bilgisi: ",self.FirstName,self.LastName,self.Tc,self.card,self.parola,
                          "siparis bilgisi:",dict["pizza_name"],dict["extra_name"],dict["total"],datetime.datetime.now()])
        print("siparisiniz alinmistir")
    except FileNotFoundError:
      with open("Orders_Database.csv", mode="w", newline="") as f:
          write = csv.writer(f, delimiter="-")
          write.writerow(["Kullanici Bilgisi: ",self.FirstName,self.LastName,self.Tc,self.card,self.parola,
                          "siparis bilgisi:",dict["pizza_name"],dict["extra_name"],dict["total"],datetime.datetime.now()])
      print("siparisiniz alinmistir")
    
if __name__ == "__main__":
  main()