# Normal vs Binomial distrubution
from numpy import random
x = random.poisson(lam=2, size=10)
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()