# Pareto Distribution
# Buyut:2x3 shape:2 pareto dağılım örneği
from numpy import random
x = random.pareto(a=2, size=(2, 3))
print(x)

# Buyut:2x3 shape:2 pareto dağılım örneği
from numpy import random
x = random.pareto(a=2, size=(2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()