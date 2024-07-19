import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Veri setini oluştur
np.random.seed(0)
X = np.sort(np.random.rand(80, 1) * 5, axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - np.random.rand(16))

# Eğitim ve test setlerine böl
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.95, test_size=0.05, random_state=0)

# Modeli oluştur ve eğit
regressor = DecisionTreeRegressor(max_depth=3)
regressor.fit(X_train, y_train)

# Tahmin yap
y_train_pred = regressor.predict(X_train)
y_test_pred = regressor.predict(X_test)

# Hata hesapla
train_error = mean_squared_error(y_train, y_train_pred)
test_error = mean_squared_error(y_test, y_test_pred)

print("Eğitim hatası:", train_error)
print("Test hatası:", test_error)

# Grafikleri çiz
plt.figure()
plt.scatter(X_train, y_train, s=20, edgecolor="black", c="darkorange", label="Eğitim verisi")
plt.scatter(X_test, y_test, s=20, edgecolor="black", c="cornflowerblue", label="Test verisi")
plt.plot(X, regressor.predict(X), color="yellowgreen", label="Model tahminleri", linewidth=2)
plt.xlabel("data")
plt.ylabel("hedef")
plt.title("Karar Ağacı Regressor")
plt.legend()
plt.show()
