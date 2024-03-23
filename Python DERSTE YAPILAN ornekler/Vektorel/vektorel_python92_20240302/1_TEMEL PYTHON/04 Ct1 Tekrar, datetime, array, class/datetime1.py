import datetime
print("Tarih saat =", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print("Tarih saat =", datetime.datetime.now().strftime("%Y"))
a = datetime.datetime.now().strftime("%Y")
a = int(a)+5
print (a)