# ANN Model ve tahmin
import numpy as np; import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, r2_score, roc_auc_score, roc_curve, classification_report
import warnings; warnings.filterwarnings("ignore", category=FutureWarning) # Hatalardan kaçınmak için
warnings.filterwarnings("ignore", category=DeprecationWarning) # Hatalardan kaçınmak için
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import scale, StandardScaler

#! VERİLERİN YÜKLENİP HAZIRLANMASI
df = pd.read_csv("dataframes/diabetes.csv") # Şeker hastalığı ile ilgili veri setimizi içe aktarıyoruz
print("\n\ndf.head()\n",df.head())
print('\n\ndf["Outcome"].value_counts()\n',df["Outcome"].value_counts())
print('\n\ndf.describe().T\n',df.describe().T)

y = df["Outcome"]
X = df.drop(["Outcome"],axis=1)

print('\n\ny.head()\n',y.head())
print('\n\nX.head()\n',X.head())

# Verileri eğitim ve test olarak bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,random_state=42)

#! Verilerin düzenlileştirilmesi
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)

scaler.fit(X_test)
X_test = scaler.transform(X_test)

nlpc_model = MLPClassifier().fit(X_train,y_train)
print("\n\nnlpc_model.get_params()\n",nlpc_model.get_params())
y_pred = nlpc_model.predict(X_test)

#! İlkel test hatası 
# Sınıflandırma problemlerinin tahmin başarısını ölçmek için accuracy_score metriğini kullanacağız.
# accuracy_score ne kadar büyükse model o kadar başarılı demektir.
print("\n\naccuracy_score(y_test, y_pred)",accuracy_score(y_test, y_pred))
print("\n\nSınıflandırma raporu: \n",classification_report(y_test,y_pred))

#! MODEL TUNİNG
denenecek_parametreler = {"alpha":[1,5,.1,.01,.03,.005,.0001],
                          "hidden_layer_sizes":[(10,10),(100,100,100),(100,100),(3,5)]}

# mlpc = MLPClassifier(solver="lbfgs")
mlpc = MLPClassifier(solver="lbfgs",activation="logistic")
# mlpc = MLPClassifier(solver="lbfgs",activation="relu")
mlpc_cv_model = GridSearchCV(mlpc, denenecek_parametreler, cv=10, n_jobs=-1, verbose=2).fit(X_train, y_train)

print("\n\nmlpc_cv_model.get_params(): \n",mlpc_cv_model.get_params())
print("\n\nmlpc_cv_model.best_params_ : \n",mlpc_cv_model.best_params_)

#! FİNAL MODELİ
nlpc_tuned = MLPClassifier(solver="lbfgs", activation="logistic", alpha=0.0001,hidden_layer_sizes=[3,5])
y_pred = nlpc_tuned.predict(X_test)
# Accuracy score (doğruluk skoru) değerinin büyük olması modelin başarılı olduğunu gösterir.
print("\n\nTest hatası : ",accuracy_score(y_test, y_pred))
