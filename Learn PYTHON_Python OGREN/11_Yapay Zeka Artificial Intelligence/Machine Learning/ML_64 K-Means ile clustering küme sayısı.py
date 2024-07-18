import numpy as np; import pandas as pd
import seaborn as sns; import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings; warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

#! VERİLERİN YÜKLENİP HAZIRLANMASI
df = pd.read_csv("dataframes/USArrests.csv", index_col=0) # Amerikadaki suç istatistikleri
print("\n\nData frame başlığı:\n",df.head())
print("\n\nEksik gözlemler:\n",df.isnull().sum()) 
print("\n\ndf.info()\n")
df.info() # print içinde kullanınca bir şey yazmayabilir.
print("\n\nBetimsel istatistikler:\n",df.describe().T)
df.hist(figsize=(10,10)); 
plt.show()

#! CLUSTER OLUŞTURALIM
kmeans = KMeans(n_clusters=4) 
k_fit = kmeans.fit(df)
print("\n\nCluster sayısı:",k_fit.n_clusters) # cluster = küme
print("\n\nKüme merkezleri:\n",k_fit.cluster_centers_)
print("\n\nAit oldukları kümeler:\n",k_fit.labels_)

#! KÜMELERİ GÖRSELEŞTİRELİM
# İki cluster/küme üzerinden görselleştirelim. (Görüntü iki boyutlu olduğu için)
# ikiden çok bileşenli yapılarda/dataframeler bileşen analiziyle iki bileşene indirgeyebiliriz.
k_means = KMeans(n_clusters=2).fit(df)
print("\n\nCluster sayısı2:",k_means.n_clusters) # cluster = küme
kumeler = k_means.labels_
print("\n\nkumeler:\n",kumeler)

merkezler = k_means.cluster_centers_
print("\n\nmerkezler:\n",merkezler)

plt.scatter(merkezler[:,0],merkezler[:,1],c= "black", s=200, alpha=0.9)
plt.scatter(df.iloc[:,0],df.iloc[:,1],c= kumeler, s=50, cmap="viridis")
# plt.show()
# plt.scatter : saçılım grafiği, c = color c= "red", s=50 size 50
# df.iloc[:, 0] : integer location,  [:, 0] ilk sütunundaki tüm değerler, [:, 1] ikinci sütunundaki tüm değerler
# cmap (colormap), nokta renk haritası. "viridis" yeşil ve mor tonları.

#! 
print("\n\nDataframe:\n",df)
ssd = [] # uzaklık farklarının karelerinin toplamı
k = range(1,30)
for x in k:
    kmeans = KMeans(n_clusters=x).fit(df)
    ssd.append(kmeans.inertia_)

plt.plot(k, ssd, "bx-")
plt.xlabel("Farklı k değerlerine karşılık artık toplamı")
plt.title("Optimum küme sayısı için Elbow Yöntemi")
plt.show()

# Yellow brick ile görselleştirme
# pip install yellowbrick
from yellowbrick.cluster import KElbowVisualizer
kmeans=KMeans()
visu = KElbowVisualizer(kmeans, k=(2,20))
visu.fit(df)
visu.poof()

kmeans = KMeans(n_clusters=4).fit(df)
print("\n\nkmeans:\n",kmeans)
kumeler = kmeans.labels_
pd.DataFrame({"Eyaletler":df.index, "Kümeler":kumeler})
print("\n\ndf['Kume_No']\n")
11:44 te kaldım.