# Metin içinde al içeren kelimeler
import re
txt1 = "Ahmet al renkli bir şal aldı."
txt2 = "Mehmet kırmızı bir top getirdi."
print(re.findall("al", txt1))
print(re.findall("al", txt2))