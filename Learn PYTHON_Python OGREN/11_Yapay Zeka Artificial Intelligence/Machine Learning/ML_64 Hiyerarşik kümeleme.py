from scipy.cluster.hierarchy import linkage, dendrogram
import pandas as pd; import matplotlib.pyplot as plt

#! VERİLERİN YÜKLENİP HAZIRLANMASI
df = pd.read_csv("dataframes/USArrests.csv", index_col=0) # Amerikadaki suç istatistikleri
print("\n\nData frame başlığı:\n",df.head())
print("\n\nEksik gözlemler:\n",df.isnull().sum()) 
print("\n\ndf.info()\n")
df.info() # print içinde kullanınca bir şey yazmayabilir.
print("\n\nBetimsel istatistikler:\n",df.describe().T)

hc_complete = linkage(df, "complete")
hc_avarage = linkage(df, "average")

# df.hist(figsize=(10,5)); 
plt.figure(figsize=(10,10)) # Büyüklük
plt.title("Hiyerarşik Kümeleme Dendrogramı (default)")
plt.xlabel("Gözlem brimleri")
plt.ylabel("Uzaklıklar")
dendrogram(hc_complete, leaf_font_size=10);
plt.show()

plt.figure(figsize=(10,5))
plt.title("Hiyerarşik Kümeleme Dendrogramı (parametreli)")
plt.xlabel("Gözlem brimleri"); plt.ylabel("Uzaklıklar")
dendrogram(hc_complete, truncate_mode="lastp", p=9, show_contracted=True, leaf_font_size=10);
plt.show()

plt.figure(figsize=(15,10))
plt.title("Hiyerarşik Kümeleme Dendrogramı (hc_average)")
plt.xlabel("Gözlem brimleri"); plt.ylabel("Uzaklıklar")
dendrogram(hc_avarage, leaf_font_size=10);
plt.show()