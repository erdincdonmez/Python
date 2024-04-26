import pandas as pd
import numpy as np
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

veri = pd.read_csv("Learn PYTHON_Python OGREN/11_Yapay Zeka Artificial Intelligence/NLP Dogal Dil Isleme/datasets/gender_classifier.csv", encoding="latin1")

print(veri.head())

# mevcut veri setinden yeni bir veri seti oluşturma
veri1 = pd.concat([veri.gender, veri.description], axis=1)

veri1.dropna(inplace=True)  # eksik verileri temizleme
veri1.reset_index(drop=True, inplace=True)

# verilere gender yerine 0 ve 1 ekleme
veri1.gender = [1 if i == "female" else 0 for i in veri1.gender]
print(veri1.head())

ps = PorterStemmer()

nltk.download("stopwords")  # stopwords indirme

stop_words = set(stopwords.words("english"))

liste = []
for j in range(1000):
    metin = re.sub("[^a-zA-Z]", " ", veri1.description[j])
    metin = metin.lower()
    metin = metin.split()
    metin = [ps.stem(i) for i in metin if not i in stop_words]  # burada stop_words kullanılmalı
    metinSon = " ".join(metin)
    liste.append(metinSon)

# CountVectorizer ile metin vektörlerini oluşturma
kf = CountVectorizer(max_features=10000)  # max_features parametresi eklenmeli
x = kf.fit_transform(liste).toarray()
y = veri1.iloc[:1000, 0].values

# Eğitim ve test veri setlerini oluşturma
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=33)

# GaussianNB sınıflandırıcısını oluşturma ve eğitme
gn = GaussianNB()
gn.fit(xtrain, ytrain)

# Test verileri üzerinde tahmin yapma
yhead = gn.predict(xtest)

# Confusion matrix oluşturma
cm = confusion_matrix(ytest, yhead)
print(cm)

# Model doğruluğunu hesaplama
print(gn.score(xtest, ytest))
