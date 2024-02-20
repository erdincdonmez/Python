# join : dizileri birleştirme
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print("\narr3:\n",arr3)

# tek eksen (axis) birleştirme
arr4 = np.array([[1, 2], [3, 4]])
arr5 = np.array([[5, 6], [7, 8]])
arr6 = np.concatenate((arr4, arr5))
arr7 = np.concatenate((arr4, arr5), axis=1)
print("\nnormal birleşmiş arr6:\n",arr6)
print("\ntek eksende birleşmiş arr7:\n",arr7)