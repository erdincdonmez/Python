import pandas as pd
import numpy as np

veri = pd.read_csv("Learn PYTHON_Python OGREN/11_Yapay Zeka Artificial Intelligence/NLP Dogal Dil Isleme/datasets/gender_classifier.csv",encoding="latin1")

print (veri.head())

# mevcut veri setinden yeni bir veri seti oluşturma
veri1 = pd.concat([veri.gender,veri.description],axis=1) 

veri1.dropna(inplace=True) # eksik verileri temizleme
print(veri1.head())

# verilere gender yerine 0 ve 1 ekleme
veri1.gender=[1 if i=="female" else 0 for i in veri1.gender]
print(veri1.head())

import re
metin = re.sub("[^a-zA-Z]"," ",veri1.description[1])
print(metin)
harfler = metin.lower()
print(harfler)









