# RF random forest ile sınıflandırma problemlerinde Model ve tahmin
import numpy as np; import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, r2_score, roc_auc_score, roc_curve, classification_report
import warnings; warnings.filterwarnings("ignore", category=FutureWarning) # Hatalardan kaçınmak için
warnings.filterwarnings("ignore", category=DeprecationWarning) # Hatalardan kaçınmak için
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from xgboost import XGBClassifier

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
xgb_model = XGBClassifier().fit(X_train,y_train)
print("\n\nxgb_model.get_params()\n",xgb_model.get_params())
y_pred = xgb_model.predict(X_test)

#! İlkel test hatası 
# Sınıflandırma problemlerinin tahmin başarısını ölçmek için accuracy_score metriğini kullanacağız.
# accuracy_score ne kadar büyükse model o kadar başarılı demektir.
print("\n\naccuracy_score(y_test, y_pred)",accuracy_score(y_test, y_pred))
# print("\n\nSınıflandırma raporu: \n",classification_report(y_test,y_pred))

#! MODEL TUNİNG
denenecek_parametreler = {"learning_rate":[.1,.01,.001],
                          "n_estimators":[100,500,1000],
                          "max_depth":[3,5,7],
                          "subsample":[.6,.8,1]}

xgb = XGBClassifier()
xgb_cv_model = GridSearchCV(xgb, denenecek_parametreler, cv=10, n_jobs=-1, verbose=2).fit(X_train, y_train)

print("\n\nxgb_cv_model.get_params(): \n",xgb_cv_model.get_params())
print("\n\nxgb_cv_model.best_params_ : \n",xgb_cv_model.best_params_)

#! FİNAL MODELİ
xgb_tuned = XGBClassifier(max_depth=7, learning_rate=.001,n_estimators=500,subsample=.6).fit(X_train, y_train)
y_pred = xgb_tuned.predict(X_test)
# # Accuracy score (doğruluk skoru) değerinin büyük olması modelin başarılı olduğunu gösterir.
print("\n\nFinal modeli test hatası : ",accuracy_score(y_test, y_pred))

#! DEĞİŞKEN ÖNEM DÜZEYLERİ
print("\n\nxgb_tuned.get_params() : \n",xgb_tuned.get_params())
print("\n\nxgb_tuned.feature_importances_ : \n",xgb_tuned.feature_importances_)

feature_imp = pd.Series(xgb_tuned.feature_importances_, index=X_train.columns).sort_values(ascending=False)
sns.barplot(x=feature_imp,y=feature_imp.index)
plt.xlabel("Değişken önem skoru")
plt.ylabel("Değişkenler")
plt.title("Değişken Önem Düzeyleri")
plt.show()
