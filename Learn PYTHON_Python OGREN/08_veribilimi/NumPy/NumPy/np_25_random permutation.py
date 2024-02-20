# Permutations (dizi elemanlarının Rastgele Karıştırılması)
from numpy import random
import numpy as np
arr = np.array([7, 2, 3, 4, 5])
print("Orjinal dizi                   : ",arr)
random.shuffle(arr) #orijinal dizide değişiklikler yapar.
print("shuffle ile karıştırılmış dizi : ",arr)
print("shuffle sonrası Orjinal dizi   : ",arr)

arr = np.array([8, 2, 3, 4, 5])
arr1= random.permutation(arr)
print("\nOrjinal dizi                       : ",arr)
print("permutation ile karıştırılmış dizi : ",arr1)
print("permutation sonrası orjinal dizi   : ",arr)
