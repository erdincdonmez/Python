import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import SVR

from warnings import filterwarnings
filterwarnings('ignore')

# SVR (Support Vector Regression/Destek Vektör Regresyonu)

# Hatalardan kaçınma
import warnings; filterwarnings('ignore')

# Veri yükleme ve hazırlama
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

# SVR Modeli kurulumu
svr_model = SVR(kernel="linear").fit(X_train,y_train)
# svr_model = SVR(kernel="rbf").fit(X_train,y_train) # rbf Radial Bases Function

# Modele göz atalım
print("\nModel Parametreleri:\n", svr_model.get_params())
print("\nintercept_:", svr_model.intercept_)
print("\ncoef_:", svr_model.coef_) # coef_ sadece kernel linear olduğunda çalışır
print("\nsvr_model içinden alınabilecekler: \n",dir(svr_model))

# Tahmin etme
svr_model.predict(X_train)[0:5]
y_pred = svr_model.predict(X_train)
print("\n\ntahmin edilen (eğitim verisinden):\n",y_pred)
svr_model.predict(X_test)[0:5]
y_pred = svr_model.predict(X_test)
print("\n\ntahmin edilen (test verisinden):\n",y_test)

# SVR modeliyle elde edilen tahminlerin ilkel test hatası
# hkokkd hata kareler ortalamasının karekökü değeri
hkokkd = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n\nHata kareler ortalaması karekökü değeri: ",hkokkd)

# SVR algoritmasının c (control parameter) değeri
# control parametresi: modelin çalışmasını etkileyen, kullanıcı tarafından belirlenen parametrelerdir. ceza parametresi / karışıklık parametresi olarak ta adlandırılır.

# RMSE = []
# for k in range(11):
#     k = k+1
#     knn_model = KNeighborsRegressor(n_neighbors=k).fit(X_train, y_train)
#     y_pred = knn_model.predict(X_test)
#     rmse = np.sqrt(mean_squared_error(y_test, y_pred))
#     RMSE.append(rmse)
#     print("\nk=",k,"için RMSE değeri:",rmse)
   
 # GridSearchCV ile control parametresini otomatik belirleme
svr_params = {"C":[.1,.5,1,3]}
# knn = KNeighborsRegressor()
# svr_cv_model = GridSearchCV(svr_model, svr_params, cv = 2).fit(X_train, y_train) # !!! cv parametresi için 3-5 gibi bir değerin üzerine çıktığında hesaplama süresi 10dkyı geçebilir..
svr_cv_model = GridSearchCV(svr_model, svr_params, cv = 2, verbose=2, n_jobs=-1).fit(X_train, y_train) # !!! verbose=2, yapılan işlemleri göster, n_jobs=-1 işlemciyi max performansta kullan.
print("svr_cv_model.best_params_ : ",svr_cv_model.best_params_)
 
#  final model
svr_tuned = SVR(kernel="linear",C=0.5).fit(X_train, y_train)
y_pred = svr_tuned.predict(X_test)
# final modelinin test hatası
fmth = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n\nFinal modeli test hatası:",fmth)



