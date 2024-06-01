# Adım-1: Dataframe’i içe aktaralım.
# https://www.statlearning.com/resources-python
# pip install pandas
import pandas as pd
# df = pd.read_csv("dataframes/Advertising.csv")
df = pd.read_csv("Advertising.csv") 
df = df.iloc[:,1:len(df)] # index sütunu için
# print(df.head())
# print(df.info) # dataframe içeriği
print(df.info()) # dataframe hakkında bilgi