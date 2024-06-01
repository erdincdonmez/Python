# Adım-2: Dataframe’i görselleştirelim.
# pip install pandas
import pandas as pd
# df = pd.read_csv("dataframes/Advertising.csv")
df = pd.read_csv("Advertising.csv") 
df = df.iloc[:,1:len(df)] # index sütunu için
print(df.info()) # dataframe hakkında bilgi
# pip install seaborn
import seaborn as sns
sns.jointplot(x="TV", y="sales", data=df, kind = "reg")

import matplotlib.pyplot as plt
plt.show()