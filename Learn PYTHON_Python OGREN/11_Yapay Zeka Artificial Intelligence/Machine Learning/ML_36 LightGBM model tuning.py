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

#! MODEL TUNING
lgbm_model = LGBMRegressor()
print("\n\nlgb_model parametreleri:\n",lgbm_model.get_params())

lgbm_tune_parametreleri = {"learning_rate":[.01,.1,.5,1],
                           "n_estimator":[20,40,100,200,500,1000],
                           "max_depth":range(1, 11)}
lgbm_cv_model = GridSearchCV(lgbm_model,lgbm_tune_parametreleri,cv=10,n_jobs=-1,verbose=2).fit(X_train, y_train)

print("\n\nÖnerilen en iyi parametreler:\n",lgbm_cv_model.best_params_)

lgbm_tuned_model = LGBMRegressor(learning_rate=.1, max_depth=6,n_estimators=20).fit(X_train,y_train)

y_pred = lgbm_tuned_model.predict(X_test)

hko = np.sqrt(mean_squared_error(y_test, y_pred)) 

print("\n\nFinal modeli test hatası:",hko)