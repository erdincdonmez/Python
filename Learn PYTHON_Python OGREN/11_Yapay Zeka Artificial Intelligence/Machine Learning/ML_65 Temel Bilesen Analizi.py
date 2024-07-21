import pandas as pd; import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

#! VERİLERİN YÜKLENİP HAZIRLANMASI
df = pd.read_csv("dataframes/Hitters.csv", index_col=0) # Baseboolcular veriseti
df.dropna(inplace=True)
df = df._get_numeric_data()
print("\n\nData frame başlığı:\n",df.head())
df = StandardScaler().fit_transform(df)
print("\n\ndf[0:5,0:5] : \n",df[0:5,0:5])

#! Veri setini (en önemli) iki bileşene indirgeyeceğiz.
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_fit = pca.fit_transform(df)

bilesen_df = pd.DataFrame(data = pca_fit, columns=["birinci_bilesen","ikinci_bilesen"])
print("\n\nbilesen_df : \n",bilesen_df)
print("\n\npca.explained_variance_ratio_ : \n",pca.explained_variance_ratio_)
print("\n\npca.components_[1] : \n",pca.components_[1])

#! Optimum bileşen sayısını bulma
pca = PCA().fit(df)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel("Bileşen sayısı")
plt.ylabel("Kümülatif varyans oranı")
plt.show()





