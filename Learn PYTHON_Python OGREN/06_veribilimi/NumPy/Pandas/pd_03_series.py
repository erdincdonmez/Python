
# SERIES
# Pandas Serisi bir tablodaki sütun gibidir.
# Her türden veriyi tutan tek boyutlu bir dizidir.

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print("İlk eleman   :",myvar[0])
print("İkinci eleman:",myvar[1])