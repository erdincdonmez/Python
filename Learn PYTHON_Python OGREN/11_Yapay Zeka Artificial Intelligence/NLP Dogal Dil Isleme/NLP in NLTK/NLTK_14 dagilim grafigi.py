# pip install matplotlib

import nltk
# nltk.download("book") # 
from nltk.book import *
import matplotlib.pyplot as plt

# İlanlardaki (text8) bazı kelimelerin kullanım sıklığı.
# text8.dispersion_plot(["woman", "lady", "girl", "gal", "man", "gentleman", "boy", "guy"])
# Sense and Sensibility by Jane Austen 1811 romanındaki bazı karakterlerin kullanım dağılımı
text2.dispersion_plot(["Allenham", "Whitwell", "Cleveland", "Combe"])

plt.show()

