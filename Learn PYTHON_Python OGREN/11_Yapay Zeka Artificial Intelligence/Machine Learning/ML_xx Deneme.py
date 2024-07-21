import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Örnek veri seti oluşturma
data = np.array([[2.5, 2.4],
                 [0.5, 0.7],
                 [2.2, 2.9],
                 [1.9, 2.2],
                 [3.1, 3.0],
                 [2.3, 2.7],
                 [2, 1.6],
                 [1, 1.1],
                 [1.5, 1.6],
                 [1.1, 0.9]])

# Veri setini DataFrame'e dönüştürme
df = pd.DataFrame(data, columns=['x', 'y'])

# PCA uygulama
pca = PCA(n_components=2)
principal_components = pca.fit_transform(df)

# PCA sonucunu DataFrame'e dönüştürme
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

# PCA sonucunu görselleştirme
plt.scatter(pca_df['PC1'], pca_df['PC2'])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA Sonucu')
plt.show()
