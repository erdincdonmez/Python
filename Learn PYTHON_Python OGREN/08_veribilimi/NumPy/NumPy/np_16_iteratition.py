# iterasyon : dizilerdeki elemanları dolaşma
import numpy as np

arr1 = np.array([1, 2, 3])
print("\ntek boyutlu dizi elemanları:")
for x in arr1: print(x)

print("\niki boyutlu dizi elemanları:")
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr2: print(x)

print("\niki boyutlu dizi TÜM elemanları:")
for x in arr2:
    for y in x: print(y)

print("\nÜç boyutlu dizinin elemanları:")
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr3: print(x)

print("\nÜç boyutlu dizinin TÜM elemanları:")
for x in arr3:
  for y in x:
    for z in y: print(z)

arr4 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nnditer ile iterasyon(tüm elemanları dolaşma)")
for x in np.nditer(arr4): print(x)

arr5 = np.array([1, 2, 3])
print("\nnditer ile veri tipi değiştirme öncesi:")
for x in np.nditer(arr5): print(x)
print("\nnditer ile veri tipi değiştirme sonrası:")
for x in np.nditer(arr5, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr6 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("\nadımlar ile atlayarak iterasyon:")
for x in np.nditer(arr6[:, ::2]): print(x)

arr7 = np.array(['a', 'b', 'c'])
print("\nndenumate ile numaralandırarak iterasyon:")
for idx, x in np.ndenumerate(arr7): print(idx, x)

arr8 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("\n2D dizide ndenumate ile numaralandırmalı iterasyon:")
for idx, x in np.ndenumerate(arr8): print(idx, x)