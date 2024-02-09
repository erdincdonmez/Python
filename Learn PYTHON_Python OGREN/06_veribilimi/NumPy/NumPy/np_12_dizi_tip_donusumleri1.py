# Dizi tipleri

import numpy as np
arr1 = np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)

arr2 = np.array(['Muz', 'Elma', 'Nar'])
print(arr2.dtype)

arr3 = np.array([1, 2, 3, 4], dtype='S')
print(arr3)
print(arr3.dtype)

arr4 = np.array([1, 2, 32, 4], dtype='S')
print(arr4)
print(arr4.dtype)

# i, u, f, S ve U için boyutu da tanımlayabiliriz.
arr5 = np.array([1, 2, 3, 4], dtype='i4')
print(arr5)
print(arr5.dtype)

# arr6 = np.array(['a', '2', '3'], dtype='i') # a dan dolayı hata verir

arr7 = np.array([1.1, 2.1, 3.1])
print("arr7.dtype :", arr7.dtype)
newarr7 = arr7.astype('i') # tür dönüştürme yapılabilir.
print(newarr7)
print("newarr.dtype :", newarr7.dtype)

arr8 = np.array([1.1, 2.1, 3.1])
print("arr8.dtype :",arr8.dtype)
newarr8 = arr8.astype(int) # int te kullanabilirsiniz.
print(newarr8)
print("newarr8.dtype :", newarr8.dtype)

arr9 = np.array([1, 0, 3])
print(arr9.dtype)
newarr9 = arr9.astype(bool) # boolean a çevirim
print(newarr9)
print(newarr9.dtype)