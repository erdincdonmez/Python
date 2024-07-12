#  XGBOOST algoritması
import numpy as np; import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore') # Hatalardan kaçınma
import xgboost; from xgboost import XGBRegressor

#! VERİ YÜKLEME ve HAZIRLAMA
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

#! MODEL KURULUMU
# windosta
# pip install xgboost 
# anaconda kullanıyorsanız ve hata aldıysanız, yönetici olarak çalıştırarak deneyin.

# macte kurulumda "The default interactive shell ..." gibi bir hata ile karşılaşırsanız
# sudo xcodebuild -license
# bilgisayar şifresini yaz, enter ile devam, agree ile kabul et.

xgb = XGBRegressor().fit(X_train,y_train)
print("\n\nxgb regresyon model parametreleri:\n",xgb.get_params())

y_pred = xgb.predict(X_test)
ilkel_test_hatasi = np.sqrt(mean_squared_error(y_test, y_pred))

print("İlkel test hatası:",ilkel_test_hatasi)

