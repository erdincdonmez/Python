# veri setini alma
import pandas as pd

# encoding ile bazı karakterlerin çıkmama sorununu çözebiliriz
veri = pd.read_csv("Learn PYTHON_Python OGREN/11_Yapay Zeka Artificial Intelligence/NLP Dogal Dil Isleme/datasets/gender_classifier.csv",encoding="latin1") 

print (veri.head())


