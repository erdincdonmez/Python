import pandas as pd

df = pd.read_csv("Advertising.csv")
df = df.iloc[:,1:len(df)]
print("\n\ndf.head()\n",df.head())
X = df.drop('sales',axis=1)
# y = df["sales"]
y = df[["sales"]] # pandas dataframe
print("\n\ny.head()\n",y.head())
print("\n\nX.head()\n",X.head())

# pip insatall statsmodel
import statsmodels.api as sm
lm = sm.OLS(y,X) # linear model
model = lm.fit()
print(model.summary())

