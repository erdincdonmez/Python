# K-Katlı cros validation yaklaşımıyla model doğrulama
import pandas as pd

df = pd.read_csv("Advertising.csv")
df = df.iloc[:,1:len(df)]
print("\n\ndf.head()\n",df.head())
X = df.drop('sales',axis=1)
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

# sınama seti
from sklearn.model_selection import train_test_split
# random_state değerini değiştirdiğimizde Eğitim Hatası ve test hatası sonuçları değişecektir.
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=99)

print("\n\nX_train.head():\n",X_train.head())
print("\n\nX_test.head():\n",X_test.head())
print("\n\ny_train.head():\n",y_train.head())
print("\n\ny_test.head():\n",y_test.head())

lm = LinearRegression()
model = lm.fit(X_train,y_train)
# Eğitim hatası
EH = np.sqrt(mean_squared_error(y_train,model.predict(X_train)))
# Test hatası
TH = np.sqrt(mean_squared_error(y_test,model.predict(X_test)))
print("\n\nEğitim Hatası:",EH)
print("\nTest Hatası:",TH)

from sklearn.model_selection import cross_val_score
cvs = cross_val_score(model, X_train, y_train, cv=10, scoring="neg_mean_squared_error")
cvsm = np.mean(-cross_val_score(model,X_train, y_train, cv=10, scoring ="neg_mean_squared_error"))
cvsm = mse = np.mean(-cross_val_score(model,X_train, y_train, cv=10, scoring ="neg_mean_squared_error"))
cvsmr = rmse = np.sqrt(np.mean(-cross_val_score(model,X_train, y_train, cv=10, scoring ="neg_mean_squared_error")))
print("\ncross_val_score                : ",cvs)
print("\ncross_val_score mean mse       : ",mse)
print("\ncross_val_score mean root rmse : ",rmse)
# Sınama seti ile cros validation karşılaştırması
vs = rmse = np.sqrt(np.mean(-cross_val_score(model,X, y, cv=10, scoring ="neg_mean_squared_error")))
print("\nSınama ve K-Katlı karşılaştırması : ",vs)


