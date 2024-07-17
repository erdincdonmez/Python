import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Veri setini yükleme
df = pd.read_csv("dataframes/USArrests.csv", index_col=0)

# Veriyi standardize etme
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# PCA uygulama
pca = PCA(n_components=2)  # 2 bileşene indirgeme
principal_components = pca.fit_transform(df_scaled)

# Yeni PCA veri seti oluşturma
df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

# PCA sonuçlarını görselleştirme
plt.figure(figsize=(8, 6))
plt.scatter(df_pca['PC1'], df_pca['PC2'], c='blue', edgecolor='k')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA ile İndirgenmiş Veri')
plt.grid()
plt.show()
