# Farklı lambda değerlerine karşılık
# beta bağımsız değişkenin nasıl değişiğini görelim
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import cross_val_score

# Baseboll oyuncularının verileri
df = pd.read_csv("dataframes/Hitters.csv")
df = df.dropna()
dms = pd.get_dummies(df[['League','Division','NewLeague']])
y = df["Salary"]
X_ = df.drop(["Salary",'League','Division','NewLeague'], axis=1).astype('float64')
X = pd.concat([X_, dms[['League_N','Division_W','NewLeague_N']]], axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

print("\n\ndf.head():\n",df.head())
print("\n\ndf.head(): ",df.shape)

# ridge_model = Ridge(alpha=0.1).fit(X_train,y_train)
# ridge_model = Ridge(alpha=5).fit(X_train,y_train)
# print("\n\nridge_model:\n",ridge_model)
# print("\n\nridge_model.coef_:\n",ridge_model.coef_)
# print("\n\nridge_model.intercept_:\n",ridge_model.intercept_)

# print(np.linspace(10,-2,100))
# lambdalar = 10**np.linspace(10,-2,100)*0.5
# print("\n\lambdalar:\n",lambdalar)

# ridge_model = Ridge()
# katsayilar = []
# for i in lambdalar:
#     ridge_model.set_params(alpha=i)
#     ridge_model.fit(X_train, y_train)
#     katsayilar.append(ridge_model.coef_)

# print(katsayilar)
# ax = plt.gca()
# ax.plot(lambdalar, katsayilar)
# ax.set_xscale("log")
# plt.show() 
ridge_model = Ridge().fit(X_train, y_train)
y_pred = ridge_model.predict(X_train)
print("\n\ny_pred[0:10]:\n",y_pred[0:10])
print("\n\ny_train[0:10]:\n",y_train[0:10])

# train/eğitim verisi hatası
RMSE = np.sqrt(mean_squared_error(y_train, y_pred))
print("\n\nRMSE:",RMSE)

cv_sonuc = np.sqrt(np.mean(-cross_val_score(ridge_model, X_train, y_train, cv = 10, scoring="neg_mean_squared_error")))
# np.sqrt(np.mean(cross_val_score(ridge_model, X_train, y_train, cv=10, scoring="mean_squared_error")))
print("\n\nCros Validation sonucu:",cv_sonuc)

# test verisi hatası
y_pred = ridge_model.predict(X_test)
RMSE = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n\nRMSE:",RMSE)
