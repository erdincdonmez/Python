# Hatalı hücreleri düzeltme
import pandas as pd
print("\n\nVeriler:\n")
df = pd.read_csv('data3.csv')
print(df.to_string()) 

print("\n\nVeri düzeltilmiş hali:\n")
df.loc[7, 'sira'] = 45
print(df.to_string()) 

df = pd.read_csv('data3.csv')
print("\n\n120'den büyükleri 120 yap:\n")
for x in df.index:
  if df.loc[x, "Sure"] > 120:
    df.loc[x, "Sure"] = 120
print(df.to_string()) 


