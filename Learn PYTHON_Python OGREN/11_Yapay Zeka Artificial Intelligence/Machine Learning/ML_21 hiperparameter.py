import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor

# Veri setini yükleme ve hazırlama
df = pd.read_csv("dataframes/Hitters.csv")
df = df.dropna() # Eksik değerleri kaldırma
dms = pd.get_dummies(df[['League', 'Division', 'NewLeague']])
y = df["Salary"]
X_ = df.drop(["Salary", 'League', 'Division', 'NewLeague'], axis=1).astype('float64')
X = pd.concat([X_, dms[['League_N', 'Division_W', 'NewLeague_N']]], axis=1)

# Veriyi eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Model ve hiperparametrelerin belirlenmesi
model = DecisionTreeRegressor()
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10]
}

# Grid search ile en iyi hiperparametreleri bulma
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='r2')
grid_search.fit(X_train, y_train)

# En iyi hiperparametreler ve model performansı
print("En İyi Hiperparametreler:", grid_search.best_params_)
print("En İyi R2 Skoru:", grid_search.best_score_)

