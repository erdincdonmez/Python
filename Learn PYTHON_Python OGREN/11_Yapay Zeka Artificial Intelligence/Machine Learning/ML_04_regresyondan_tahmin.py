# Adım-3: Dataframe’i görselleştirelim.
# pip install pandas
import pandas as pd
# df = pd.read_csv("dataframes/Advertising.csv")
df = pd.read_csv("Advertising.csv") 
df = df.iloc[:,1:len(df)] # index sütunu için
print(df.info()) # dataframe hakkında bilgi
# pip install seaborn
import seaborn as sns
# sns.jointplot(x="TV", y="sales", data=df, kind="reg")

import matplotlib.pyplot as plt
# plt.show()

from sklearn.linear_model import LinearRegression
X = df[["TV"]] # Bağımsız değişken
y = df[["sales"]] # Bağımlı değişken

print("\n\nBağımsız değişken:\n",X.head())
print("\n\nBağımlı değişken :\n",y.head())

reg = LinearRegression() # Model nesnesi oluşturma

model = reg.fit(X,y) # modeli kurıyoruz.
print ("\n\nstr(model):",str(model))
print ("\n\ndir(model):",dir(model))
print ("\n\nmodel.intercept_ :",model.intercept_) # Sabit ya da beta0 değeri
print ("\n\nmodel.coef_      :",model.coef_) # beta1 katsayısı

print ("\n\nmodel.score(X,y) :",model.score(X,y)) # rkare = model skoru
# rkare : Bağımlı değişkendeki değişikliğin bağımsız değişkenlerin açıklayabilme oranıdır.

g = sns.regplot(x="TV", y="sales", data=df,ci=50,scatter_kws={'color':'r','s':9})
g.set_title(f"Model Denklemi: Sales = {model.intercept_}+TV*{model.coef_}")
g.set_ylabel("Satış sayısı")
g.set_xlabel("TV Reklam Harcama Miktarı")
plt.xlim(-10,310) # x exeni limitleri
plt.ylim(bottom=0) # y ekseni başlangıcı

plt.show() # regresyon eğrisini çizdirelim

print("model.predict([[165]]):",model.predict([[165]])) # x bağımsız değişken değeri
reklam_harcamalari = [[5],[15],[30]]
print("5,15,30 değerleri için tahmin sonuçları:\n",model.predict(reklam_harcamalari)) 






