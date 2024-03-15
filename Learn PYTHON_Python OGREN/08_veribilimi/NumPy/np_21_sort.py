# Array Sort
# Orijinal diziyi değiştirmeden, bir kopyas döndürür.
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) # numerik sıralama

arr = np.array(['muz','elma','armut'])
print(np.sort(arr)) # string sıralama

arr = np.array([True, False, True])
print(np.sort(arr)) # bolean sıralam

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr)) # 2D array sıralama


