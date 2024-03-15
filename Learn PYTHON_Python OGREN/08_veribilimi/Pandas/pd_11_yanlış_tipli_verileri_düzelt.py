# Hatalı hücreleri düzeltme
import pandas as pd
df = pd.read_csv('data3.csv')
print("\n\nVeriler:\n")
# print(df)
# print(df.to_string()) 

df = pd.read_csv('data3.csv')
print("\n\nDüzelmeyen verinin satırınn silinmesi:\n")
df.dropna(subset=['Tarih'], inplace = True)
print(df.to_string())

# df = pd.read_csv('data3.csv')
print("\n\nHatalı hücrelerin düzeltilmiş hali:\n")
df['Tarih'] = pd.to_datetime(df['Tarih'])
print(df.to_string())



