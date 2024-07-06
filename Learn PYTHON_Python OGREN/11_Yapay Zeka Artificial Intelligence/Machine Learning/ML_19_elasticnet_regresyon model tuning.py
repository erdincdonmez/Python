import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt

# Veri yükleme ve hazırlama
df = pd.read_csv("dataframes/Hitters.csv")
df = df.dropna() # DataFrame'de eksik (NaN) değeri içeren satırları kaldır
dms = pd.get_dummies(df[['League', 'Division', 'NewLeague']])
y = df["Salary"]
X_ = df.drop(["Salary", 'League', 'Division', 'NewLeague'], axis=1).astype('float64')
X = pd.concat([X_, dms[['League_N', 'Division_W', 'NewLeague_N']]], axis=1)

# Veriyi eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Veri setine bakalım
print("\n\ndf.head():", df.head())
print("\n\ndf.shape():", df.shape)

# Elasticnet modelini kuralım
enet_model = ElasticNet().fit(X_train, y_train)

print("\n\nElasticNet model:\n", enet_model)
print("\n\nElasticNet model intercept:\n", enet_model.intercept_)
print("\n\nElasticNet model katsayılar:\n", enet_model.coef_)

# Tahmin yapalım
X_train_tahmin = enet_model.predict(X_train)[0:10]
print("\n\nX_train_tahmin:",X_train_tahmin)

X_test_tahmin = enet_model.predict(X_test)[0:10]
print("\n\nX_test_tahmin:",X_test_tahmin)

# Test hatalarına bakalım.
y_pred = enet_model.predict(X_test) # Tahmin edilen değerler
ilkel_test_hatasi = np.sqrt(mean_squared_error(y_test, y_pred)) # Hata kareler ortalamasının karekökü

# Optimize edilmememiş modelimizin test hatasını yazdıralım.
print("\n\nilkel_test_hatasi:",ilkel_test_hatasi)

# Modeller ilerledikçe test hatasının düşmesini beklemek doğru değil.
# Her modelin farklı bir probleme daha iyi çözüm üretebilir.

# modelin açıklanabilirliğini ifade için r2_score kullanlır.
# Bağımsız değişkenlerin bağımlı değişkene -yüzdelik olarak-etkisini açıklar.
r2_degeri = r2_score(y_test, y_pred)
print("\n\nr2_degeri:",r2_degeri)

# alfalar = 10**np.linspace(10,-2,100)*0.5

enet_cv_model= ElasticNetCV(cv=10).fit(X_train, y_train)
# enet_cv_model= enetCV(alphas = alfalar, cv=10, max_iter = 100000).fit(X_train, y_train)
print("\n\nenet_cv_model.alpha_ : ", enet_cv_model.alpha_)
print("\n\nenet_cv_model.intercept_ : ", enet_cv_model.intercept_)
print("\n\nenet_cv_model.coef_ : ", enet_cv_model.coef_)

# Bulmuş olduğumuz optimum alpha/lambda değeri ile Final modeli oluşturma
# enet_tuned = ElasticNet().set_params(alpha = enet_cv_model.alpha_).fit(X_train, y_train)
enet_tuned = ElasticNet(alpha = enet_cv_model.alpha_).fit(X_train,y_train)

# Final modelinin test seti hatası
y_pred = enet_tuned.predict(X_test)
mse = np.sqrt(mean_squared_error(y_test,y_pred))
print("\n\nmse: ",mse)

# # Değişkenlerin Katsayıları. Katsayıların bağımlı değişkene atkisi
# sk = pd.Series(lasso_tuned.coef_, index=X_train.columns)
# print("\n\nsk: ",sk)

