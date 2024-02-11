# Analyzing DataFrames
import pandas as pd
df = pd.read_csv('data.csv')
print("\n\nbaşlıkla birlikte 10 satır göster")
print(df.head(10))
print("\n\nbaşlıkla birlikte ilk 5 satır:")
print(df.head())
print("\n\nSon 5 satır:")
print(df.tail())
print("\n\nSon 10 satır:")
print(df.tail(10))
print("\n\nVeri bilgisi:\n")
print(df.info())

