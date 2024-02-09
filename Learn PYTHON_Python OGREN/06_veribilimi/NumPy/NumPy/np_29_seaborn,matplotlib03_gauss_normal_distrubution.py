# Gauss dağılımı (normal dağılım)
from numpy import random

a = random.normal(size=(2, 3))
print(a)
b = random.normal(loc=1, scale=2, size=(2, 3))
print(b)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)
plt.show()
