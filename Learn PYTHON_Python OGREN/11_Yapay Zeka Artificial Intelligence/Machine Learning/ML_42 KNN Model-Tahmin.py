# KNN K-Nearest Neighbors / K En yakın komşu
import numpy as np; import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, r2_score, roc_auc_score, roc_curve, classification_report
import warnings; warnings.filterwarnings("ignore", category=FutureWarning) # Hatalardan kaçınmak için
warnings.filterwarnings("ignore", category=DeprecationWarning) # Hatalardan kaçınmak için
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

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
knn_model = KNeighborsClassifier().fit(X,y)
y_pred = knn_model.predict(X) # Bölmeden tahmin

print("\n\nTahmin edilen bağımlı değişken (y) değerleri: \n",y_pred)
print("\n\nconfusion_matrix: \n",confusion_matrix(y,y_pred))
print("\n\naccuracy_score: ",accuracy_score(y,y_pred))
print("\n\nclassification_report: \n",classification_report(y,y_pred))

logit_roc_auc = roc_auc_score(y, knn_model.predict(X))
# fpr = False Positive Rate, tpr = True Positive Rate
# roc_curve = roc eğrisi. Model performansını değerlendirmek için bir referans.
fpr, tpr, tresholds = roc_curve(y, knn_model.predict_proba(X)[:,1])
plt.figure()
plt.plot(fpr, tpr, label="AUC (area=%0.2f)" % logit_roc_auc)
plt.plot([0,1],[0,1],'r--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver oprerating characteristic")
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,random_state=42)

knn_model = KNeighborsClassifier().fit(X_train,y_train)
print("\n\nknn_model.get_params()\n",knn_model.get_params())
y_pred = knn_model.predict(X_test)

# Sınıflandırma problemlerinin tahmin başarısını ölçmek için accuracy_score metriğini kullanacağız.
# accuracy_score ne kadar büyükse model o kadar başarılı demektir.
print("\n\naccuracy_score(y_test, y_pred)",accuracy_score(y_test, y_pred))
# Sınıflandırma problemlerinde hiper parametrelerin optimum değerleri için cros validation yöntemini kullanacağız.
# Modelleri train seti ile eğitirken cross validation yöntemini kullanacağız
#  Dışarıda bıraktığımız test setini performans ölçümü için kaullanacağız.
hatalar = cross_val_score(knn_model, X_test, y_test)
print("\n\nHatalar : ", hatalar)

hatalar = cross_val_score(knn_model, X_test, y_test, cv=10)
print("\n\nHatalar (10lu) : ", hatalar)

hatalar = cross_val_score(knn_model, X_test, y_test, cv=10).mean()
print("\n\nHatalar (10lunun ortalaması) : ", hatalar)

print("\n\nclassification_report: \n",classification_report(y_test,y_pred))
