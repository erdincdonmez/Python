import numpy as np

# İki diziyi toplama
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
result = np.add(arr1, arr2)  # np.add() ufunc'ını kullanma
print(result)  # [ 6  8 10 12]

# Bir dizi üzerinde trigonometrik işlemler
angles = np.array([0, np.pi/2, np.pi])
sin_values = np.sin(angles)
print(sin_values)  # [0. 1. 0.]

# Bir diziyi bir sayıyla çarpma
arr = np.array([1, 2, 3, 4])
scaled_arr = np.multiply(arr, 2)
print(scaled_arr)  # [2 4 6 8]

# Bir dizielemanlarının karesini bulma
arr = np.array([1, 2, 3, 4])
scaled_arr = np.multiply(arr, arr)
print(scaled_arr)  # [ 1 4 9 16]
