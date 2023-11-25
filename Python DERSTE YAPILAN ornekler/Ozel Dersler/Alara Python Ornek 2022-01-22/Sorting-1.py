a = [5, 1, 4, 3]
print ("Sıralanacak veri :",a)  
print ("Sıralanmış veri  :",sorted(a))  
print ("Sıralanmamış veri:",a)  

from datetime import datetime

baslangic = datetime.now()
for i in range (80000000):
  print(i)
bitis = datetime.now()
print ("Başlama: ",baslangic)
print ("Bitiş: ",bitis)
print ("Fark: ",bitis-baslangic)
