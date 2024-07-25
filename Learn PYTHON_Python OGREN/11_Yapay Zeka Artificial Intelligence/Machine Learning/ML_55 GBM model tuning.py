# gbm random forest ile sınıflandırma problemlerinde Model ve tahmin
import numpy as np; import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, r2_score, roc_auc_score, roc_curve, classification_report
import warnings; warnings.filterwarnings("ignore", category=FutureWarning) # Hatalardan kaçınmak için
warnings.filterwarnings("ignore", category=DeprecationWarning) # Hatalardan kaçınmak için
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import GradientBoostingClassifier

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

#! MODEL KURMA 
gbm_model = GradientBoostingClassifier().fit(X_train,y_train)
print("\n\ngbm_model.get_params()\n",gbm_model.get_params())
y_pred = gbm_model.predict(X_test)

#! İlkel test hatası 
# Sınıflandırma problemlerinin tahmin başarısını ölçmek için accuracy_score metriğini kullanacağız.
# accuracy_score ne kadar büyükse model o kadar başarılı demektir.
print("\n\naccuracy_score(y_test, y_pred)",accuracy_score(y_test, y_pred))
# print("\n\nSınıflandırma raporu: \n",classification_report(y_test,y_pred))

#! MODEL TUNİNG
denenecek_parametreler = {"learning_rate":[.1,.01,.001,.5],
                          "n_estimators":[100,300,500,1000],
                          "max_depth":[3,5,7,8]}

gbm = GradientBoostingClassifier()
gbm_cv_model = GridSearchCV(gbm, denenecek_parametreler, cv=10, n_jobs=-1, verbose=2).fit(X_train, y_train)

print("\n\ngbm_cv_model.get_params(): \n",gbm_cv_model.get_params())
print("\n\ngbm_cv_model.best_params_ : \n",gbm_cv_model.best_params_)

#! FİNAL MODELİ
gbm_tuned = GradientBoostingClassifier(max_depth=5, min_samples_split=20).fit(X_train, y_train)
y_pred = gbm_tuned.predict(X_test)
# # Accuracy score (doğruluk skoru) değerinin büyük olması modelin başarılı olduğunu gösterir.
print("\n\nFinal modeli test hatası : ",accuracy_score(y_test, y_pred))

#! DEĞİŞKEN ÖNEM DÜZEYLERİ
print("\n\ngbm_tuned.get_params() : \n",gbm_tuned.get_params())
print("\n\ngbm_tuned.feature_importances_ : \n",gbm_tuned.feature_importances_)

feature_imp = pd.Series(gbm_tuned.feature_importances_, index=X_train.columns).sort_values(ascending=False)
sns.barplot(x=feature_imp,y=feature_imp.index)
plt.xlabel("Değişken önem skoru")
plt.ylabel("Değişkenler")
plt.title("Değişken Önem Düzeyleri")
plt.show()