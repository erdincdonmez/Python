import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, Lasso
from sklearn.linear_model import RidgeCV, LassoCV
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

# Lasso modelini kuralım
lasso_model = Lasso().fit(X_train, y_train)

print("\n\nLasso model:\n", lasso_model)
print("\n\nLasso model intercept:\n", lasso_model.intercept_)
print("\n\nLasso model katsayılar:\n", lasso_model.coef_)

# Farklı lambda değerlerine karşılık katsayılar
lasso = Lasso()
coefs = [] # katsayılar
# alphas = np.random.randint(1, 1000, 10)  # Sıfır ve negatif değerlerden kaçınmak için alt sınır 1 yapıldı
alphas = 10**np.linspace(10, -2, 100)*0.5  # Sıfır ve negatif değerlerden kaçınmak için alt sınır 1 yapıldı
for a in alphas:
    lasso.set_params(alpha=a)
    lasso.fit(X_train, y_train)
    coefs.append(lasso.coef_)

X_train_tahmin = lasso_model.predict(X_train)[0:5]
X_test_tahmin = lasso_model.predict(X_test)[0:5]
print("\n\nX_train_tahmin:",X_train_tahmin)
print("\n\nX_test_tahmin:",X_test_tahmin)

# Test hatalarına bakalım.
y_pred = lasso_model.predict(X_test) # Tahmin edilen değerler
ilkel_test_hatasi = np.sqrt(mean_squared_error(y_test, y_pred)) # Hata kareler ortalamasının karekökü

# Optimize edilmememiş modelimizin test hatasını yazdıralım.
print("\n\nilkel_test_hatasi:",ilkel_test_hatasi)

# Modeller ilerledikçe test hatasının düşmesini beklemek doğru değil.
# Her modelin farklı bir probleme daha iyi çözüm üretebilir.

# r2 değeri (r kare değeri) modelin açıklanabilirliğini ifade eder.
# Bağımsız değişkenlerin bağımlı değişkene -yüzdelik olarak-etkisini açıklar. 
r2_degeri = r2_score(y_test, y_pred)
print("\n\nr2_degeri:",r2_degeri)

lasso_cv_model = LassoCV(cv=10, max_iter=100000).fit(X_train,y_train)
print("\n\nlasso_cv_model.alpha_ : ",lasso_cv_model.alpha_)

lasso_tuned = Lasso().set_params(alpha = lasso_cv_model.alpha_).fit(X_train, y_train)
lasso_tuned = Lasso(alpha = lasso_cv_model.alpha_).fit(X_train, y_train)

np.sqrt(mean_squared_error(y_test, y_pred))


