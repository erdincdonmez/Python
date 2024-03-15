# Serbestlik derecesi 2 ve boyutu 2x3 olan ki kare dağılımı
from numpy import random
x = random.chisquare(df=2, size=(2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()