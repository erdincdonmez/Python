import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Veri yükleme ve hazırlama
df = pd.read_csv("dataframes/Hitters.csv")
df = df.dropna()
dms = pd.get_dummies(df[['League', 'Division', 'NewLeague']])
y = df["Salary"]
X_ = df.drop(["Salary", 'League', 'Division', 'NewLeague'], axis=1).astype('float64')
X = pd.concat([X_, dms[['League_N', 'Division_W', 'NewLeague_N']]], axis=1)

# Veriyi eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Verileri normalize etme
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model oluşturma ve eğitim
ridge_model = Ridge().fit(X_train_scaled, y_train)
y_pred_train = ridge_model.predict(X_train_scaled)

# Eğitim verisi hatası
train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
print("Eğitim Verisi RMSE:", train_rmse)

# Cross-validation ile model değerlendirme
cv_score = np.sqrt(np.mean(-cross_val_score(ridge_model, X_train_scaled, y_train, cv=10, scoring="neg_mean_squared_error")))
print("Cross Validation RMSE:", cv_score)

# Test verisi hatası
y_pred_test = ridge_model.predict(X_test_scaled)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
print("Test Verisi RMSE:", test_rmse)

# Farklı lambda değerlerine karşılık katsayı değişimi
lambdalar1 = np.random.randint(0,1000,100)
lambdalar2 = 10**np.linspace(10, -2, 100) * 0.5

ridgecv = RidgeCV(alphas=lambdalar1, scoring="neg_mean_squared_error", cv=10)
ridgecv.fit(X_train_scaled, y_train)
print("Optimum Lambda:", ridgecv.alpha_)

# Farklı lambda değerlerine karşılık katsayı değişimi
katsayilar = []

for i in lambdalar2:
    ridge_model.set_params(alpha=i)
    ridge_model.fit(X_train_scaled, y_train)
    katsayilar.append(ridge_model.coef_)

# Katsayıları çizdirme
ax = plt.gca()
ax.plot(lambdalar2, katsayilar)
ax.set_xscale("log")
plt.xlabel("Lambda (log scale)")
plt.ylabel("Katsayılar")
plt.title("Lambda Değerlerine Göre Katsayı Değişimi")
plt.show()
