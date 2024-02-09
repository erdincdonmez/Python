# Simple aritmetic
import numpy as np

arr1 = np.array([10, 12, 24, 26, 14, -15])
arr2 = np.array([ 3,  3,  4,  3,  7,  3])
print(f"\narr1 : {arr1}\narr2 : {arr2}")

print("\nadd      :",np.add(arr1, arr2))

newarr = np.subtract(arr1, arr2)
print("\nsubtract :",newarr)

newarr = np.multiply(arr1, arr2)
print("\nmultiply :",newarr)

newarr = np.divide(arr1, arr2)
print("\ndivide   :", newarr)

print("\npower(*) :",np.power(arr1,arr2))
# 60 ve 33, 12 ve 22'yi 0 döndürdü neden?

print("\nmod (%)  :",np.mod(arr1, arr2))

newarr = np.remainder(arr1, arr2)
print("\nremainder:", newarr)

print("\ndivmod   :",np.divmod(arr1,arr2))

newarr = np.absolute(arr1)
print("\nabsolute :", newarr)

