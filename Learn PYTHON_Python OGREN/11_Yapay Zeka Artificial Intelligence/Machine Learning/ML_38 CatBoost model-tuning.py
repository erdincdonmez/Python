# CatBoost Category Boosting
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
# pip install catboost

#! MODEL KURULUMU
from catboost import CatBoostRegressor
catb_model = CatBoostRegressor().fit(X_train, y_train)   
# print("\n\ncatb_model:\n",catb_model.get_params())

y_pred = catb_model.predict(X_test)                         
ilkel_test_hatasi = np.sqrt(mean_squared_error(y_test, y_pred))
print("ilkel_test_hatasi",ilkel_test_hatasi)

#! MODEL TUNING
catb_model = CatBoostRegressor()
print("\n\nlgb_model parametreleri:\n",catb_model.get_params())

catboost_tune_parametreleri = {"iterations":[200,500,100],
                           "learning_rate":[.01,.1],
                           "depth":[3,6,8]}
catboost_cv_model = GridSearchCV(catb_model,catboost_tune_parametreleri,cv=5,n_jobs=-1,verbose=2).fit(X_train, y_train)

print("\n\nÖnerilen en iyi parametreler:\n",catboost_cv_model.best_params_)

catboost_tuned_model = CatBoostRegressor(learning_rate=.1, max_depth=6,n_estimators=20).fit(X_train,y_train)

y_pred = catboost_tuned_model.predict(X_test)

hko = np.sqrt(mean_squared_error(y_test, y_pred)) 

print("\n\nFinal modeli test hatası:",hko)