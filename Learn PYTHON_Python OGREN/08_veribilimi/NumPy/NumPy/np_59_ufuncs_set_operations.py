# Set Operations
# Matematikte küme benzersiz öğelerin koleksiyondur. Kesişme, birleştirme ve fark gibi işlemleri vardır.
import numpy as np

# NumPy'de Setler Oluştur. Sadece 1 boytulu diziler olabilir.
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
print(f"{arr1} {arr2} Birleşimi: ",newarr)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print("Kesşimi:",newarr)

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print("Fark:",newarr)

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print("Simetrik fark:",newarr)







