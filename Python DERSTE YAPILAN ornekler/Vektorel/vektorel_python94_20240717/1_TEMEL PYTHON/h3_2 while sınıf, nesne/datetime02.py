import datetime
print("Bugün:", datetime.date.today())
tarih = datetime.date.today()
# print("Bu yıl:", tarih[0:4]) # type string olmadığı için olmaz.
print("Bu yıl:", str(tarih)[0:4])
print(f"Formatlanmış tarih: {str(tarih)[0:4]}xx{str(tarih)[5:7]}")

import datetime, time, os
for a in range (100000):
  # print("Saat:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
  time.sleep(1)
  os.system("cls")
  print("Saat:", datetime.datetime.now().strftime("%H:%M:%S %a"))

