# Join (dizi birleştirme)
import numpy as np

arr8 = np.array([1, 2, 3])
arr9 = np.array([4, 5, 6])
arr10 = np.stack((arr8, arr9), axis=1)
print("\nstack (axis=1):\n",arr10)
arr11 = np.hstack((arr8, arr9))
print("\nhstack(horizontal) :\n",arr11)
arr12 = np.vstack((arr8, arr9))
print("\nvstack(vertical) :\n",arr12)
arr13 = np.dstack((arr8, arr9))
print("\ndstack(dimentional) :\n",arr13)