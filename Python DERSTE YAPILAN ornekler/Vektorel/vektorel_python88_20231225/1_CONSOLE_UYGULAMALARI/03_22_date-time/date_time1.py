import datetime
print("Bugün :", datetime.date.today())
print("Şimdi :", datetime.datetime.now())
tarih = datetime.date.today()
print("Tarih : ", tarih)
simdi = datetime.datetime.now()
print(simdi.strftime("%m/%d/%Y %H:%M:%S"))
print(simdi.strftime("%m,%M/%d,%D/%y,%Y %H:%M:%S"))

