# Logistic distrubution
# Ortalaması 1 ve stddev 2.0 olan bir lojistik dağılımdan 2x3 örnek çizin
from numpy import random
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)