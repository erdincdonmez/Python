import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import scale
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

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

# CART Classification and Regression Tree / Sınıflandırma ve Karar Ağaçları Algoritması
#! model kurulumu
rf_model = RandomForestRegressor(random_state = 42).fit(X_train, y_train)
print("\n\nRandom forest modelinin parametreleri:\n",rf_model.get_params())

# tahmin yapalım
y_pred = rf_model.predict(X_test)
# ilkel test hatasına bakalım (haata karelerinin ortamasının karekökü)
# Gerçek değerler (y_test) ile model tarafından tahmin edilen değerler (y_pred) arasındaki farkların karesinin ortalamasının karekökü
fokkk = np.sqrt(mean_squared_error(y_test,y_pred))
print("\n\nFarkların ortalamasının karesinin karekökü: ",fokkk)

rf_model = RandomForestRegressor(random_state=42).fit(X_train, y_train)
print("rf_model parametreleri:", rf_model.get_params())

# Burada yazılan deneme parametreleri uzmanların makalelerinden alınan değerlerdir.
# Başka değerlerle de denenebilir tabii ki.
rf_parametreleri = {"max_depth":[5,8,10],
                    "max_features":[2,5,10],
                    "n_estimators":[200,500,1000,2000],
                    "min_sample_split":[2,10,80,100]}

GridSearchCV(rf_model, rf_parametreleri, cv=10, n_jobs=-1,verbose=2).fit(X_train, y_train)
dk.5:19

