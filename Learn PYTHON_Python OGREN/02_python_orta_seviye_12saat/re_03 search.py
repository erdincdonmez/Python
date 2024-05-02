# Metin içinde arama
import re
txt = "Ahmet al renkli bir şal aldı."
aa = re.search("\s", txt)
print("İlk boşluğun bulunduğu yer:", aa.start())
bb = re.search("Mehmet", txt)
print(bb)
cc = re.search("şal", txt)
print(cc)