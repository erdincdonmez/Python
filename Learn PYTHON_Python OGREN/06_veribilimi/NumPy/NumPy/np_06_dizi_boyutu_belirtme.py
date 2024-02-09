# Dizilerin kaç boyutlu olduğunu öğrenelim.
import numpy as np
arr = np.array(35)
print("1-0 boyutlu dizi: ",arr)
arr1 = np.array([33, 34, 35, 36])
print("2-tek boyutlu dizi: ", arr1)
arr2 = np.array([[33,30,35], [4,5,6]])
print("3-İki boyutlu dizi: ",arr2)
xxx = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print("4- Üç boyutlu dizi: ",xxx)

# Dizilerin kaç boyutlu olduğunu öğrenelim.
print("1.nin boyut sayısı:", arr.ndim)
print("2.nin boyut sayısı:", arr1.ndim)
print("3.nin boyut sayısı:", arr2.ndim)
print("4.nin boyut sayısı:", xxx.ndim)

arr3 = np.array([1, 2, 3, 4], ndmin=5)
print("yeni dizi: ", arr3)
print('Dizinin boyut sayısı :', arr3.ndim)
