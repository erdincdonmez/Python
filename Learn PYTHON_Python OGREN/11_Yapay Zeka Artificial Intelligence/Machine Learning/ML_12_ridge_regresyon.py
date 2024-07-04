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

# Baseboll oyuncularının(Hitters) verileri  
df = pd.read_csv("dataframes/Hitters.csv")
df = df.dropna()
dms = pd.get_dummies(df[['League','Division','NewLeague']])
y = df["Salary"]
X_ = df.drop(["Salary",'League','Division','NewLeague'], axis=1).astype('float64')
X = pd.concat([X_, dms[['League_N','Division_W','NewLeague_N']]], axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

print("\n\ndf.head():\n",df.head())
print("\n\ndf.shape(): ",df.shape)

# ridge_model = Ridge(alpha=0.1).fit(X_train,y_train)
ridge_model = Ridge(alpha=5).fit(X_train,y_train)
print("\n\nridge_model:\n",ridge_model)
print("\n\nridge_model.coef_:\n",ridge_model.coef_)
print("\n\nridge_model.intercept_:\n",ridge_model.intercept_)

print(np.linspace(10,-2,100))
lambdalar = 10**np.linspace(10,-2,100)*0.5 
# linspace ile belli düzende rasgele sayılar elde ediyoruz.
print("\n\nlambdalar:\n",lambdalar)

ridge_model = Ridge()
katsayilar = []
for i in lambdalar: 
    ridge_model.set_params(alpha=i)
    ridge_model.fit(X_train, y_train)
    katsayilar.append(ridge_model.coef_)

# print("\n\nKatsayılar:",katsayilar,"\n")
print("\n\nKatsayılar:")
for x in katsayilar:
    print(x)
ax = plt.gca()
ax.plot(lambdalar, katsayilar)
ax.set_xscale("log")
plt.show()



