
dizi = [2,4,7,8]
# print(dizi)
# for x in dizi:
#     print(x,end=" ")

import numpy as np

# arr1 = np.array([1, 2, 3])
# print("\ntek boyutlu dizi elemanları:")
# print(arr1)
# for x in arr1: print(x)

# arr4 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print("\nnditer ile iterasyon(tüm elemanları dolaşma)")
# for x in np.nditer(arr4): print(x)

arr5 = [[1, 2], [3, 4]]
# print(arr5)
for a in arr5:
    for b in a:
        print(arr5[a,b])