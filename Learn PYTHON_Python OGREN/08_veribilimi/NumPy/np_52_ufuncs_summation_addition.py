# summation and addition
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
print("arr1   :", arr1)
print("arr1   :", arr2)

newarr = np.add(arr1, arr2)
print("add(arr1, arr2)           :",newarr)

newarr = np.sum([arr1, arr2])
print("sum([arr1, arr2])         :",newarr)

newarr = np.sum([arr1, arr2], axis=1)
print("sum([arr1, arr2], axis=1) :",newarr)

# Kümülatif kümelenerek/birikerek artmadır. Verilerin birikerek üst üste eklenmesidir.
newarr = np.cumsum(arr1)
print("cumsum(arr1) ile kümülatif:",newarr)


