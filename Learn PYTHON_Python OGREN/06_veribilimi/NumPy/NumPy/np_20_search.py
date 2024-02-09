# Array Search
import numpy as np

arr = np.array([1,2,3,4,5,7,4,41,2,3,4,5,6,7,8,9,7])
print(f"\nDizi({len(arr)} elemanlı) : ", arr)
x = np.where(arr == 4)
print("\nBulunan 4'lerin yeri .where(arr == 4)          :",x)

x = np.where(arr%2 == 0)
print("\nBulunan çift sayıların yeri .where(arr%2 == 0) :",x)

x = np.where(arr%2 == 1)
print("\nBulunan tek sayıların yeri .where(arr%2 == 1)  :",x)

arr1 = np.array([1,2,4,5,7,8,9])
x = np.searchsorted(arr1, 5)
print("\nDizi : ",arr1)
print(".searchsorted(arr1, 5) : ",x)
x = np.searchsorted(arr1, 5, side='left') # soldan ilk index 0'dan başlar.
print(".searchsorted(arr1, 5) side='left' : ",x)
x = np.searchsorted(arr1, 5, side='right') # sağdan ilk index 1 olur.
print(".searchsorted(arr1, 5) side='right': ",x)

x = np.searchsorted(arr1, [2, 4, 6])
print(".searchsorted(arr1, [2, 4, 6]) : ",x)