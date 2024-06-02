import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Örnek veri seti
data = {'TV Reklamı': [230.1, 44.5, 17.2, 151.5, 180.8],
        'Satış': [22.1, 10.4, 9.3, 18.5, 12.9]}
df = pd.DataFrame(data)

# Bağımsız ve bağımlı değişkenler
X = df[['TV Reklamı']]
y = df['Satış']

# Veriyi eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluşturma ve eğitme
model = LinearRegression()
model.fit(X_train, y_train)

# Test verisi üzerinde tahmin yapma
y_pred = model.predict(X_test)

# Modelin performansını değerlendirme
mse = mean_squared_error(y_test, y_pred)
print(f'MSE=Mean Squared Error/Hata Karelerin Ortalaması: {mse}')


