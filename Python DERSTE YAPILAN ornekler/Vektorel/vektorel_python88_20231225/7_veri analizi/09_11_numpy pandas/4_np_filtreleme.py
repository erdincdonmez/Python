# filter
import numpy as np

filtrelenecek = np.array([41,42,43,44])
x = [True, False, True, False]
newarr = filtrelenecek[x]
print(newarr)

# yeniDizi = filtrelenecek > 42
yeniDizi = filtrelenecek % 2 == 0
newarr = filtrelenecek[yeniDizi]
print(yeniDizi)
print(newarr)
