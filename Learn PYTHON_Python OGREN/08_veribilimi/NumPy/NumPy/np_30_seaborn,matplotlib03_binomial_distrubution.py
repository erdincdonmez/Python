# Binomial dağılım (binom dağılımı)
from numpy import random

# n- Deneme sayısı.
# p- her denemenin gerçekleşme olasılığı (yazı-tura için 0.5)
# size- Döndürülen dizinin şekli.
x = random.binomial(n=10, p=0.5, size=10)
print("Yazı-tura için 10 deneme verildiğinde 10 veri noktası oluşturulur:\n",x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()