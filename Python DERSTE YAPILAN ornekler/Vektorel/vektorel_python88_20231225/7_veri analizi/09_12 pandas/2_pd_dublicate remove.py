# Tekrarlı hücreler
import pandas as pd
print("\n\nVeriler:\n")
df = pd.read_csv('data.csv')
print(df.to_string())
# Listelendiğinde 11 ve 12.satırların aynı olduğu görülecektir.
print("\n\nHücrelerin tekrar durumu:\n")
print(df.duplicated())

print("\n\nTekrarlıların kaldılmış hali:\n")
df.drop_duplicates(inplace = True)
print(df.to_string())