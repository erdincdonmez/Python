# satır ve sütunlar
import numpy as np

arr1 = np.arange(1,21).reshape(5,4)
print (arr1)

# print("\nBirinci satır => arr1[0]   : ",arr1[2])
# print("\nİkinci satır  => arr1[1]   : ",arr1[1])
# print("\nİlk iki satır => arr1[0:2] : \n",arr1[0:2])
# print("\nBirinci sütun => arr1[:,0] : ",arr1[:,0])
# print("\nİkinci sütun  => arr1[:,1] : ",arr1[:,1]) 
print("\nEleman        => arr1[2,1] : ",arr1[4,3])  