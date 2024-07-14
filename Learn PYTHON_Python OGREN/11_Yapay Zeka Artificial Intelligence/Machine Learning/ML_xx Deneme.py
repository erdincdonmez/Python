from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt

# Örnek veri oluşturma
from sklearn.datasets import make_circles
X, y = make_circles(n_samples=100, factor=0.1, noise=0.1)

# RBF kernel kullanarak SVM modeli eğitme
model = SVC(kernel='rbf', gamma='auto')
model.fit(X, y)

# Veri noktalarını ve karar sınırını görselleştirme
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plt.show()
