# Hatalı hücreleri düzeltme
import pandas as pd
df = pd.read_csv('data.csv')
print("\n\nVeriler:\n")
print(df.to_string())

print("\n\nHatalı hücrelerin düzeltilmiş hali:\n")
df['Tarih'] = pd.to_datetime(df['Tarih'])
print(df.to_string())

##df = pd.read_csv('data.csv')
##print("\n\nDüzelmeyen veri satırının silinmesi:\n")
##df.dropna(subset=['Tarih'], inplace = True)
##print(df.to_string())
