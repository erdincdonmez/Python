# sub ile değiştirme
import re; txt = "Ahmet al renkli bir şal aldı."
print(re.sub("\s", "x", txt)) # Boşlukları x yap
print(re.sub(" ", "_", txt)) # Boşlukları _ yap
print(re.sub(" ", "   ", txt)) # Boşlukları 3 boşluk yap
print(re.sub("al", "red", txt)) # al ları red yap