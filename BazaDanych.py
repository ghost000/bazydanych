# !/usr/bin/python
from Widoki.KlientWidokModel import KlientWidokModel
from Widoki.PizzaWidokModel import PizzaWidokModel
from Widoki.SkladnikiWidokModel import SkladnikiWidokModel
from Widoki.ZamowieniaWidokModel import ZamowieniaWidokModel
from Widoki.ZawartoscWidokModel import ZawartoscWidokModel

obj1 = KlientWidokModel()
obj2 = PizzaWidokModel()
obj3 = SkladnikiWidokModel()
obj4 = ZamowieniaWidokModel()
obj5 = ZawartoscWidokModel()


for element in obj1.getKlienci():
    print(element)
for element in obj2.getPizze():
    print(element)
for element in obj3.getSkladniki():
    print(element)
for element in obj4.getZamowienia():
    print(element)
for element in obj5.getZawartosci():
    print(element)
