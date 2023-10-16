from datetime import datetime

baslangic = datetime.now()
for i in range (80000000):
  print(i)
bitis = datetime.now()
print ("Başlama: ",baslangic)
print ("Bitiş: ",bitis)
print ("Fark: ",bitis-baslangic)
