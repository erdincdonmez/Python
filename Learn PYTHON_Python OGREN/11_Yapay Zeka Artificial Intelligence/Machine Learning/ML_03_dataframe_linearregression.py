# Adım-3: Dataframe’i görselleştirelim.
# pip install pandas
import pandas as pd
# df = pd.read_csv("dataframes/Advertising.csv")
df = pd.read_csv("Advertising.csv") 
df = df.iloc[:,1:len(df)] # index sütunu için
print(df.info()) # dataframe hakkında bilgi
# pip install seaborn
import seaborn as sns
sns.jointplot(x="TV", y="sales", data=df, kind = "reg")

# import matplotlib.pyplot as plt
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







