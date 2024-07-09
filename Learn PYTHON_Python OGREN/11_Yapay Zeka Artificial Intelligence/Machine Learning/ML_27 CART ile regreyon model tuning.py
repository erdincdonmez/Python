import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import scale
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

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
X_train = pd.DataFrame(X_train["Hits"])
X_test = pd.DataFrame(X_test["Hits"])

#! cart_modeli = DecisionTreeRegressor() # en ilkel şekli
cart_modeli = DecisionTreeRegressor(max_leaf_nodes = 10)

cart_modeli.fit(X_train, y_train)
print("\n\ncart modeli:",cart_modeli)

X_grid = np.arange(min(np.array(X_train)), max(np.array(X_train)), 0.01)
X_grid = X_grid.reshape((len(X_grid),1))

#! Grafik ile görselleştirelim
plt.scatter(X_train, y_train, color = 'red') # scatter : saçılım grafiği
plt.plot(X_grid, cart_modeli.predict(X_grid), color='blue')

plt.title('CART Regresyon Agaci')
plt.xlabel("Atış Sayıı(Hits)")
plt.ylabel("Maaşı(Salary)")
# plt.show()

#! tahmin yapalım (tek değişkenli tahmin)
cart_modeli.predict(X_test)[0:5]

y_pred = cart_modeli.predict(X_test)
hko = np.sqrt(mean_squared_error(y_test, y_pred))
print ("\nHata kareleri ortalaması:", hko)

#! Çok değişkenli tahmin için
df = pd.read_csv("dataframes/Hitters.csv") # Basebolla oyuncaları veri seti
df = df.dropna() # DataFrame'de eksik (NaN) değeri içeren satırları kaldır
dms = pd.get_dummies(df[['League', 'Division', 'NewLeague']])
y = df["Salary"]
X_ = df.drop(["Salary", 'League', 'Division', 'NewLeague'], axis=1).astype('float64')
X = pd.concat([X_, dms[['League_N', 'Division_W', 'NewLeague_N']]], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

cart_modeli = DecisionTreeRegressor().fit(X_train, y_train)
y_pred = cart_modeli.predict(X_test)
hko = np.sqrt(mean_squared_error(y_test, y_pred))
print ("\nHata kareleri ortalaması (çok değişkenli):", hko)

#! Model tuning
print("\n\ncart_modeli parametreleri:",cart_modeli.get_params())
cart_modeli = DecisionTreeRegressor(max_depth=5).fit(X_train, y_train)
y_pred = cart_modeli.predict(X_test)
hko = np.sqrt(mean_squared_error(y_test, y_pred))
print (f"\nHata kareleri ortalaması (hiper parametreli): {hko:.2f}" )

# help(cart_modeli)
# dir(cart_modeli)
# print(cart_modeli.__doc__)

cart_params = {"max_depth": [2,3,4,5,10,20],
               "min_samples_split":[2,10,5,30,50,10]}

cart_modeli = DecisionTreeRegressor()
cart_cv_model = GridSearchCV(cart_modeli, cart_params, cv=10).fit(X_train, y_train)
print("\n\nEn iyi parametreler: ",cart_cv_model.best_params_)

#! Final modeli
cart_tuned = DecisionTreeRegressor(max_depth=5, min_samples_split=50).fit(X_train, y_train)

y_pred = cart_tuned.predict(X_test)
hko = np.sqrt(mean_squared_error(y_test, y_pred))
print("Hata kareler ortalaması(final):",hko)
