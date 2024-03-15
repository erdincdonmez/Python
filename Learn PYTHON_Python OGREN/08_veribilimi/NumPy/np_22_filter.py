# filter 
import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

print("Klasik yöntem ile 42'den büyük olanlar")
filter_arr = []
for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

print("\nNumPy ile filtreleme")
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

print("Klasik yöntem ile çift sayıları alma")
filter_arr = []
for element in arr:
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

print("NumPy ile Çift sayıları filtreleme")
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)