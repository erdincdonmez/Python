import pandas as pd

df = pd.read_csv("Advertising.csv")
df = df.iloc[:,1:len(df)]
print("\n\ndf.head()\n",df.head())
X = df.drop('sales',axis=1)
# y = df["sales"]
y = df[["sales"]] # pandas dataframe
print("\n\ny.head()\n",y.head())
print("\n\nX.head()\n",X.head())

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
model = lm.fit(X,y)
print("model.intercept_",model.intercept_) # taban katsayısı
print("model.coef_",model.coef_) # bağımsız değişken katsayıları
reklamlar = [[30],[10],[40]]
reklamlar = pd.DataFrame(reklamlar).T
print("\n\nmodel.predict() : ",model.predict(reklamlar))

from sklearn.metrics import mean_squared_error
print("\n\ny.head()\n",y.head())
print("\n\nmodel.predict(X)[0:10]\n",model.predict(X)[0:10])
MSE = mean_squared_error(y,model.predict(X))
print("\n\nMSE:",MSE)
import numpy as np
RMSE = np.sqrt(MSE)
print("\n\nRMSE:",RMSE)


