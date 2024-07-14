# SVM Model ve tahmin ve optimizasyonu (tuning)
import numpy as np; import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, r2_score, roc_auc_score, roc_curve, classification_report
import warnings; warnings.filterwarnings("ignore", category=FutureWarning) # Hatalardan kaçınmak için
warnings.filterwarnings("ignore", category=DeprecationWarning) # Hatalardan kaçınmak için
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.svm import SVC

#! VERİLERİN YÜKLENİP HAZIRLANMASI
df = pd.read_csv("dataframes/diabetes.csv") # Şeker hastalığı ile ilgili veri setimizi içe aktarıyoruz
print("\n\ndf.head()\n",df.head())
y = df["Outcome"]
X = df.drop(["Outcome"],axis=1)
# Verileri eğitim ve test olarak bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,random_state=42)

svm_model = SVC().fit(X_train,y_train)
print("\n\nsvm_model.get_params()\n",svm_model.get_params())
y_pred = svm_model.predict(X_test)

#! İlkel test hatası 
# Sınıflandırma problemlerinin tahmin başarısını ölçmek için accuracy_score metriğini kullanacağız.
# accuracy_score ne kadar büyükse model o kadar başarılı demektir.
print("\n\naccuracy_score(y_test, y_pred)",accuracy_score(y_test, y_pred))

#! MODEL TUNING
deneme_parametreleri = {"C":np.arange(1,10), "kernel":["linear","rbf"]}
svm_cv_model = GridSearchCV(svm_model, deneme_parametreleri, cv=5, n_jobs=-1, verbose=2).fit(X_train, y_train)

print("\n\nsvm_cv_model.best_score_ : ",svm_cv_model.best_score_)
print("\n\nsvm_cv_model.best_params_ : ",svm_cv_model.best_params_)

#! FİNAL MODELİ 
svm_tuned = SVC(C=2, kernel="linear").fit(X_train, y_train)
y_pred = svm_tuned.predict(X_test)
print("\n\naccuracy_score(X_test, y_pred) : ",accuracy_score(X_test, y_pred))
