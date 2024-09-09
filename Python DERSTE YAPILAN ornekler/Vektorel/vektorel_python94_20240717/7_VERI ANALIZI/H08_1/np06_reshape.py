import numpy as np
arr1 = np.arange(9)
print("Dizi :\n",arr1)
arr1 = arr1.reshape(3,3)

tersi = arr1[::-1]
print("Dizi :\n",arr1)
print("Tersi:\n",tersi)