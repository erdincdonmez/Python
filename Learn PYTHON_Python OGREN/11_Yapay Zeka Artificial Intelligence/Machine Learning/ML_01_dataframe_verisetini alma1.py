# Adım-1: Dataframe’i içe aktaralım.
# https://www.statlearning.com/resources-python
# pip install pandas
import pandas as pd
# df = pd.read_csv("dataframes/Advertising.csv")
# df = pd.read_csv("Advertising.csv") 
df = pd.read_csv("dataframes\CalismaMiktarlari.csv") 
# df = df.iloc[:,1:len(df)] # index sütunu için
print("\n\ndf.head():\n",df.head())
print("\n\ndf.info():\n",df.info()) # dataframe hakkında bilgi
