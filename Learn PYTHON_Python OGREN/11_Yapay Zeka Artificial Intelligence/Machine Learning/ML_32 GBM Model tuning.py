# GBM Gradient Boosting Machine
import numpy as np; import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
import warnings; warnings.filterwarnings('ignore') # Hatalardan kaçınma

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
print("\n\nX_train verisinin ilk 5 satırı:\n", X_train.head())

# GBM Gradient Boosting Machine algoritması
# model kurulumu
gbm_model = GradientBoostingRegressor().fit(X_train, y_train)
print("\n\nGBM modelinin parametreleri:\n", gbm_model.get_params())

# tahmin yapalım
y_pred = gbm_model.predict(X_test)
# ilkel test hatasına bakalım (hata karelerinin ortamasının karekökü)
# Gerçek değerler (y_test) ile model tarafından tahmin edilen değerler (y_pred) arasındaki farkların karesinin ortalamasının karekökü
fokkk = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n\nFarkların ortalamasının karesinin karekökü: ", fokkk)

# print("\n\ndir(gbm_model):\n",dir(gbm_model))

# Buradaki parametrelerin çokluğu işlemciyi daha çok yoracaktır.
# Parametre yazarken bunu göz önünde bulundurunuz.
# Öğrenme amaçlı çalışmalar için colab gibi araçlar kullanabilirsiniz.
gbm_tune_parametreleri = {
    "learning_rate": [0.001, 0.1, 0.01],
    "max_depth": [3, 5, 8],
    "n_estimators": [100, 200, 500],
    "subsample": [1, 0.5, 0.8],
    "loss": ["squared_error", "absolute_error", "quantile"]
}

gbm_model = GradientBoostingRegressor().fit(X_train, y_train)
gbm_cv_model = GridSearchCV(gbm_model, gbm_tune_parametreleri, cv=10, n_jobs=-1, verbose=2).fit(X_train, y_train)
print("\n\ngbm_cv_model.get_params():", gbm_cv_model.get_params())
print("\n\nGridSearchCV ile en iyi parametreler:", gbm_cv_model.best_params_)

gbm_tuned = GradientBoostingRegressor(
    learning_rate=0.1,
    loss="absolute_error",
    max_depth=3,
    n_estimators=200,
    subsample=1
).fit(X_train, y_train)
y_pred = gbm_tuned.predict(X_test)
hko = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n\nTuned modelin karekökü:", hko)

# Değişkenlerin önem düzeyi.
print("Değişkenlerin önemi:", gbm_tuned.feature_importances_ * 100)

Importance = pd.DataFrame({"Importance": gbm_tuned.feature_importances_ * 100}, index=X_train.columns)
Importance.sort_values(by="Importance", axis=0, ascending=True).plot(kind="barh", color="r")

plt.xlabel("Değişkenlerin önemi grafiği")
plt.gca().legend_ = None
plt.show()
