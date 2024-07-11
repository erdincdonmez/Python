#  GBM Gradient Boosting Machine
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor

from warnings import filterwarnings
filterwarnings('ignore')

# SVR (Support Vector Regression/Destek Vektör Regresyonu)

# Hatalardan kaçınma
import warnings; filterwarnings('ignore')

#! Veri yükleme ve hazırlama
df = pd.read_csv("dataframes/Hitters.csv") # Basebolla oyuncaları veri seti
df = df.dropna() # DataFrame'de eksik (NaN) değeri içeren satırları kaldır
# one-hot encoding ile dummy (sahte/yapmacık) değişkenler oluşturuyoruz
# one-hot encoding verileri sayısal olarak ifade etme yöntemidir
dms = pd.get_dummies(df[['League', 'Division', 'NewLeague']])
y = df["Salary"]
X_ = df.drop(["Salary", 'League', 'Division', 'NewLeague'], axis=1).astype('float64')
X = pd.concat([X_, dms[['League_N', 'Division_W', 'NewLeague_N']]], axis=1)
# Veriyi eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# print("\n\nX_train verisi:\n",X_train)
print("\n\nX_train verisinin ilk 5 satırı:\n",X_train.head())

# GBM Gradient boosting machine algoritması
#! model kurulumu
gbm_model = GradientBoostingRegressor().fit(X_train, y_train)
print("\n\nGBM modelinin parametreleri:\n",gbm_model.get_params())

# tahmin yapalım
y_pred = gbm_model.predict(X_test)
# ilkel test hatasına bakalım (haata karelerinin ortamasının karekökü)
# Gerçek değerler (y_test) ile model tarafından tahmin edilen değerler (y_pred) arasındaki farkların karesinin ortalamasının karekökü
fokkk = np.sqrt(mean_squared_error(y_test,y_pred))
print("\n\nFarkların ortalamasının karesinin karekökü: ",fokkk)



