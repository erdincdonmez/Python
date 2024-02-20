# Multinominal distrubution
from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)
# Çok terimli örnekler tek bir değer üretmeyecektir! Her bir pval için bir değer üretecek.