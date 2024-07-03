import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt

# Veri yükleme ve hazırlama
df = pd.read_csv("dataframes/CalismaMiktarlari.csv")
df = df.dropna()

# Bağımsız ve bağımlı değişkenlerin belirlenmesi
y = df["Duvar"]
X = df.drop(['sn', 'Duvar'], axis=1).astype('float64')

# Veriyi eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Model oluşturma ve eğitim
ridge_model = Ridge().fit(X_train, y_train)
y_pred_train = ridge_model.predict(X_train)

# Eğitim verisi hatası
train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
print("Eğitim Verisi RMSE:", train_rmse)

# Cross-validation ile model değerlendirme
cv_score = np.sqrt(np.mean(-cross_val_score(ridge_model, X_train, y_train, cv=10, scoring="neg_mean_squared_error")))
print("Cross Validation RMSE:", cv_score)

# Test verisi hatası
y_pred_test = ridge_model.predict(X_test)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
print("Test Verisi RMSE:", test_rmse)

# Farklı lambda değerlerine karşılık katsayı değişimi
lambdalar = 10**np.linspace(10, -2, 100) * 0.5
katsayilar = []

for i in lambdalar:
    ridge_model.set_params(alpha=i)
    ridge_model.fit(X_train, y_train)
    katsayilar.append(ridge_model.coef_)

# Katsayıları çizdirme
ax = plt.gca()
ax.plot(lambdalar, katsayilar)
ax.set_xscale("log")
plt.xlabel("Lambda (log scale)")
plt.ylabel("Katsayılar")
plt.title("Lambda Değerlerine Göre Katsayı Değişimi")
plt.show()
