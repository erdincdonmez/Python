# Data Correlations (veri ilişkileri)
import pandas as pd
print("\n\nVeriler:\n")
df = pd.read_csv('data.csv')
print(df.to_string()) 

print("\n\ndf.corr() ile veri kolerasyonu:")
print("En iyi kolerasyon 1, en kötü 0\n")
print(df.corr())