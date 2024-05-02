# split ile metni bölme
import re
xxx = "Ahmet al renkli bir şal aldı."
print(re.split("\s", xxx)) # Boşluğa göre böl
print(re.split(" ", xxx)) # Boşluğa göre böl
print(re.split("a", xxx)) # a ya göre böl
print(re.split("al", xxx)) # al a göre böl
print(re.split(" ", xxx,3)) # 3.boşluk dahil böl
