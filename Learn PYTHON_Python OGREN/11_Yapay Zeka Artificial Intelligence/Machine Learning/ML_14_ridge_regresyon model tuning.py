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
 
# ridge_model = Ridge(alpha=0.1).fit(X_train,y_train) # alpha ile lambda aynı
ridge_model = Ridge().fit(X_train, y_train)
y_pred = ridge_model.predict(X_test)
print("\n\ny_pred[0:10]:\n",y_pred[0:10])
print("\n\ny_test[0:10]:\n",y_test[0:10])

lambdalar1 = np.racndom.randint(0,1000,100)
lambdalar2 = 10**np.linspace(10,-2,100)*0.5

# ridgecv = RidgeCV(alphas=lambdalar2,scoring="neg_mean_squared_error",cv=10,normalize=True)
# RidgeCV sınıfının normalize parametresi, Scikit-Learn 0.24.0 sürümünden itibaren kaldırılmıştır. 
# Bunun yerine, verilerinizi manuel olarak normalize etmeniz gerekmektedir.
ridgecv = RidgeCV(alphas=lambdalar2,scoring="neg_mean_squared_error",cv=10,normalize=True)
ridgecv.fit(X_train,y_train)
print("\n\nOptimum parametre:",ridgecv.alpha_)


