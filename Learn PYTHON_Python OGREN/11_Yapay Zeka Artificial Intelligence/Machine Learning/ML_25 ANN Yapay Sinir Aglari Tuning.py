import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

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

# ANN için standartlaştırma işlemi
# Homojen veri setlerinde aykırılıkların giderilmesi için standartlaştırma yapılır.
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
# ANN Modeli kurulumu
# mlp Multi-Layer Perceptron/Çok katmanlı algılayıcı
mlp_model = MLPRegressor().fit(X_train_scaled,y_train)
print("\n\nmlp_model:",mlp_model.get_params())
mlp_model_predict = mlp_model.predict(X_test_scaled)[0:5]
print("\n\nmlp_model_predict:",mlp_model_predict)

y_pred = mlp_model.predict(X_test_scaled)

# ilkel test hatasını hesaplayalım.
ilkel_test_hatası = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n\nilkel test hatası: ",ilkel_test_hatası)

# Model tuning
mlp_paremetreleri = {"alpha":[0.1,0.1,0.02,0.001,0.0001],"hidden_layer_sizes":[(10,20),(5,5),(100,100)]}
mlp_cv_model = GridSearchCV(mlp_model, mlp_paremetreleri, cv=5, verbose=2, n_jobs=-1).fit(X_train,y_train)

print("\nEn iyi parametreler:",mlp_cv_model.best_params_)

#  final modeli
mlp_tuned = MLPRegressor(alpha=0.1, hidden_layer_sizes=(100,100)).fit(X_train_scaled,y_train)
print("\nmlp_tuned:",mlp_tuned)
y_pred = mlp_tuned.predict(X_test_scaled)
sonuc_test_hatasi = np.sqrt(mean_squared_error(y_test, y_pred))
print("\nsonuc_test_hatasi: ",sonuc_test_hatasi)

