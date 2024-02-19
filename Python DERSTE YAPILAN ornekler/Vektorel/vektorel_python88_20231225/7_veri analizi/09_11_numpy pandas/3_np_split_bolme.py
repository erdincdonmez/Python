# split (dizi bölme)
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print("\n3'e bölünen yeni dizi :",newarr)

# newarr = np.array_split(arr, 4)
# print("\n4'e bölünen yeni dizi :",newarr)

newarr = np.array_split(arr, 3)
print("\nBölünmedeki parçaları alma")
print("1.parça :",newarr[0])
print("2.parça :",newarr[1])
print("3.parça :",newarr[2])