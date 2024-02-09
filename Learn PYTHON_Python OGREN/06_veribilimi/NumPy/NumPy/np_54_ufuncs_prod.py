# prod() bir dizideki elemanların çarpımı
import numpy as np

arr1 = np.array([3,4])
x = np.prod(arr1)
print(x)
arr2 = np.array([3,2])
x = np.prod([arr1, arr2])
print(x)
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)
newarr = np.cumprod([2,3,4])
print(newarr)

