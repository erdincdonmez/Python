# split (dizi bölme)
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print("\n3'e bölünen yeni dizi :",newarr)

newarr = np.array_split(arr, 4)
print("\n4'e bölünen yeni dizi :",newarr)

newarr = np.array_split(arr, 3)
print("\nBölünmedeki parçaları alma")
print("1.parça :",newarr[0])
print("2.parça :",newarr[1])
print("3.parça :",newarr[2])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print("\n2 boyutluyu, üç 2 boyutluya bölme :\n",newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print("\n2 boyutlu diziyi üç 2 boyutlu diziye bölme :\n",newarr)

newarr = np.array_split(arr, 3, axis=1)
print("\n2 boyutlu diziyi satırlar boyunca üç 2 boyutlu diziye bölme :\n",newarr)
# hsplit() Alternatif bir çözüm ise tersini kullanmaktır hstack()

newarr = np.hsplit(arr, 3)
print("\n2 boyutlu diziyi satırlar boyunca üç 2 boyutlu diziye bölme :\n",newarr)
# alternatif olarak vstack()ve dstack() te kullanılabilir. 