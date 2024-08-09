import datetime
print("Bugün:", datetime.date.today())
tarih = datetime.date.today()
# print("Bu yıl:", tarih[0:4]) # type string olmadığı için olmaz.
print("Bu yıl:", str(tarih)[0:4])
print(f"Formatlanmış tarih: {str(tarih)[0:4]}xx{str(tarih)[5:7]}")

from datetime import datetime
print("="*20,"\nŞimdi1 : ", datetime.now())

import datetime
print("="*20,"\nŞimdi2 : ", datetime.datetime.now())


import datetime, time, os
for a in range (100000):
  print("Şimdi =", datetime.datetime.now())
  time.sleep(1)
  os.system("cls")
