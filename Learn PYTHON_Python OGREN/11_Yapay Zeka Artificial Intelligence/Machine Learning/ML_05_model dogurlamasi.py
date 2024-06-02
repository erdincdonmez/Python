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

# print("\n\nBağımlı değerler:\n",y.head()) # head ilk 5 değeri göster
# print("\n\nİlk 5 değer için model tahmini:\n",model.predict(X)[0:5])
print("\n\nİlk 10 değer için gerçek sonuçlar:\n",y[0:9]) 
print("\n\nİlk 10 değer için model tahmini  :\n",model.predict(X)[0:9])

gercek_y = y[0:9]
tahmin_y = pd.DataFrame(model.predict(X)[0:9])
farklar  = pd.concat([gercek_y, tahmin_y],axis=1) # fark = artık = tahmin hataları
farklar.columns =["gercek_y","tahmin_y"]
print("\n\nfarklar:\n",farklar)
farklar["fark"]=farklar["gercek_y"]-farklar["tahmin_y"]
print("\n\nfarklar:\n",farklar)
farklar["hata_kareleri"]=farklar["fark"]**2
print("\n\nfarklar:\n",farklar)
import numpy as np
MSE = hataKareleriOrtalamasi = np.mean(farklar["hata_kareleri"])
print ("\n\nMSE = Hata Kareleri Ortalaması:",MSE)



