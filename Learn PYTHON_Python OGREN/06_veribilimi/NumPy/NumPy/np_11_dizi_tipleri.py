# Dizi tipleri

import numpy as np
arr1 = np.array([1, 2, 3, 4, 5]) # normal tanımlama
arr2 = np.array([1, 2, 3, 4, 5], dtype = float) # virgüllü sayı
arr3 = np.array([1, 2, 3, 4, 5], dtype = complex) # complex sayı
print(arr1)
print(arr2)
print(arr3)

# ndarray içerisine klasik python da olduğu gibi farklı türde veriler yazamıyoruz.
print (type(arr1))
print (type(arr2))
print (type(arr3))
print (arr1.dtype)
print (arr2.dtype)
print (arr3.dtype)

