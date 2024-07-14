# ANN Model ve tahmin
import numpy as np; import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, r2_score, roc_auc_score, roc_curve, classification_report
import warnings; warnings.filterwarnings("ignore", category=FutureWarning) # Hatalardan kaçınmak için
warnings.filterwarnings("ignore", category=DeprecationWarning) # Hatalardan kaçınmak için
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.neural_network import MLPClassifier

#! VERİLERİN YÜKLENİP HAZIRLANMASI
df = pd.read_csv("dataframes/diabetes.csv") # Şeker hastalığı ile ilgili veri setimizi içe aktarıyoruz
print("\n\ndf.head()\n",df.head())
print('\n\ndf["Outcome"].value_counts()\n',df["Outcome"].value_counts())
print('\n\ndf.describe().T\n',df.describe().T)

y = df["Outcome"]
X = df.drop(["Outcome"],axis=1)

print('\n\ny.head()\n',y.head())
print('\n\nX.head()\n',X.head())

# Verileri eğitim ve test olarak bölmeden model oluşturma
nlpc_model = MLPClassifier().fit(X,y); y_pred = nlpc_model.predict(X) # Bölmeden tahmin
y_pred = nlpc_model.predict(X)

print("\n\nTahmin edilen bağımlı değişken (y) değerleri: \n",y_pred)
print("\n\nconfusion_matrix: \n",confusion_matrix(y,y_pred))
print("\n\naccuracy_score: ",accuracy_score(y,y_pred))
print("\n\nclassification_report: \n",classification_report(y,y_pred))

logit_roc_auc = roc_auc_score(y, nlpc_model.predict(X))

# Verileri eğitim ve test olarak bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,random_state=42)

nlpc_model = MLPClassifier().fit(X_train,y_train)
print("\n\nnlpc_model.get_params()\n",nlpc_model.get_params())
y_pred = nlpc_model.predict(X_test)

#! İlkel test hatası 
# Sınıflandırma problemlerinin tahmin başarısını ölçmek için accuracy_score metriğini kullanacağız.
# accuracy_score ne kadar büyükse model o kadar başarılı demektir.
print("\n\naccuracy_score(y_test, y_pred)",accuracy_score(y_test, y_pred))
print("\n\nSınıflandırma raporu: \n",classification_report(y_test,y_pred))

