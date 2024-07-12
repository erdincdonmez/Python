# Random Forest (rasgele seçilmiş değişkenlerden oluşan ağaçların tahmin ortalamasıyla)
import numpy as np; import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import warnings; warnings.filterwarnings('ignore') # Hatalardan kaçınma

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
"""
'bootstrap': True, # bootstrap abligation
'ccp_alpha': 0.0, 'criterion': 'squared_error', 
'max_depth': None, # derinlik
'max_features': 1.0, # Bölünmelerde göz önünde bulundurulacak değişken sayısı
'max_leaf_nodes': None, # max yaprak nodları
'max_samples': None, 
'min_impurity_decrease': 0.0, 
'min_samples_leaf': 1, # Bir node taki min yaprak sayısı 
'min_samples_split': 2, # Bir node bölünmeden önce min gözlem sayısı
'min_weight_fraction_leaf': 0.0, 'monotonic_cst': None, 
'n_estimators': 100, # Kullanılacak olan ağaç sayısı
'n_jobs': None, 
'oob_score': False, 'random_state': 42, 'verbose': 0, 'warm_start': False
"""
# tahmin yapalım
y_pred = rf_model.predict(X_test)
# ilkel test hatasına bakalım (haata karelerinin ortamasının karekökü)
# Gerçek değerler (y_test) ile model tarafından tahmin edilen değerler (y_pred) arasındaki farkların karesinin ortalamasının karekökü
fokkk = np.sqrt(mean_squared_error(y_test,y_pred))
print("\n\nFarkların ortalamasının karesinin karekökü: ",fokkk)
