import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor

from warnings import filterwarnings
filterwarnings('ignore')

# KNN yada K-En (K-Nearest Neighbors/K-En Yakın Komşu) K komşu sayısını ifade eder.

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

# Model kurulumu
knn_model = KNeighborsRegressor().fit(X_train,y_train)

# Modele göz atalım
print("\nModel Parametreleri:\n", knn_model.get_params())
print("\nModel Komşu sayısı: ", knn_model.n_neighbors)
print("\nModel Metriği: ", knn_model.metric)
print("\nEğitim Verisi Üzerindeki Skor: ", knn_model.score(X_train, y_train))
print("\nTest Verisi Üzerindeki Skor: ", knn_model.score(X_test, y_test))
print("\nknn_model içinden alınabilecekler: \n",dir(knn_model))

# Tahmin etme
knn_model.predict(X_test)[0:5]
y_pred = knn_model.predict(X_test)
# KNN modeliyle elde edilen tahminlerin ilkel test hatası
# hkokkd hata kareler ortalamasının karekökü değeri
hkokkd = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n\nHata kareler ortalaması karekökü değeri: ",hkokkd)

# KNN algoritmasının hiperparametre değeri
# hiper parametre: modelin çalışmasını etkileyen, kullanıcı tarafından belirlenen parametrelerdir.
RMSE = []
for k in range(11):
    k = k+1
    knn_model = KNeighborsRegressor(n_neighbors=k).fit(X_train, y_train)
    y_pred = knn_model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    RMSE.append(rmse)
    print("\nk=",k,"için RMSE değeri:",rmse)
    
 # GridSearchCV ile hiperparametreyi otomatik belirleme
knn_params = {"n_neighbors":np.arange(1,30,1)}
knn = KNeighborsRegressor()
knn_cv_model = GridSearchCV(knn, knn_params, cv = 10).fit(X_train, y_train)
print("knn_cv_model.best_params_ : ",knn_cv_model.best_params_)
 
#  final model
knn_tuned = KNeighborsRegressor(n_neighbors=knn_cv_model.best_params_["n_neighbors"]).fit(X_train, y_train)
y_pred = knn_tuned.predict(X_test)
# final modelinin test hatası
fmth = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n\nFinal modeli test hatası:",fmth)

