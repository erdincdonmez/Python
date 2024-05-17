import pandas as pd
import numpy as np

veri = pd.read_csv("Learn PYTHON_Python OGREN/11_Yapay Zeka Artificial Intelligence/NLP Dogal Dil Isleme/datasets/gender_classifier.csv",encoding="latin1")

print (veri.head())

# mevcut veri setinden yeni bir veri seti oluşturma
veri1 = pd.concat([veri.gender,veri.description],axis=1) 

veri1.dropna(inplace=True) # eksik verileri temizleme
print(veri1.head())
veri1.reset_index(drop=True,inplace=True)

# verilere gender yerine 0 ve 1 ekleme
veri1.gender=[1 if i=="female" else 0 for i in veri1.gender]
print(veri1.head())

import re
metin = re.sub("[^a-zA-Z]"," ",veri1.description[1])
print(metin)
kucukHarf = metin.lower()
bol =kucukHarf.split()
print(kucukHarf)

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

import nltk
# stop=nltk.download("stopwords") # stopwords indirme

from nltk.corpus import stopwords

metin = [ps.stem(i) for i in bol if not i in set(stopwords.words("english"))]
metinSon = " ".join(metin)
print(metinSon)

liste=[]
for j in range(1000):
    metin = re.sub("[^a-zA-Z]"," ",veri1.description[j])
    metin = metin.lower()
    metin = metin.split()
    metin = [ps.stem(i) for i in bol if not i in set(stopwords.words("english"))]
    metinSon = " ".join(metin)
    liste.append(metinSon)
print(metinSon)





