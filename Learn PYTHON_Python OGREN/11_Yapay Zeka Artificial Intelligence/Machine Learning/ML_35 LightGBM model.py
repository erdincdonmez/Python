#  LightGBM algoritması
import numpy as np; import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV # cv:cross-validation/çapraz doğrulama
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings("ignore") # Hatalardan kaçınmak için

#! VERİLERİN YÜKLENİP HAZIRLANMASI
df = pd.read_csv("dataframes/Hitters.csv") # veri setimizi içe aktarıyoruz
df = df.dropna() # gereksiz verileri/satırları (NaN) datasetin dışına bırakıyoruz
dms = pd.get_dummies(df[["League","Division","NewLeague"]]) # one-code-encoding yöntemiyle sayısal veriye dönüştürüyoruz.
y = df["Salary"]
X_ = df.drop(["Salary","League","Division","NewLeague"],axis=1).astype("float64")
X = pd.concat([X_, dms[["League_N","Division_W","NewLeague_N"]]],axis=1)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.25,random_state=42)

#! KÜTÜPHANE KURULUMU
# pip install lightgbm
# conda install -c conda-forge lightgbm

#! MODEL KURULUMU
from lightgbm import LGBMRegressor
lgbm_model = LGBMRegressor().fit(X_train, y_train)   
# print("\n\nlgbm_model:\n",lgbm_model.get_params())

y_pred = lgbm_model.predict(X_test)                         
ilkel_test_hatasi = np.sqrt(mean_squared_error(y_test, y_pred))
print("ilkel_test_hatasi",ilkel_test_hatasi)
