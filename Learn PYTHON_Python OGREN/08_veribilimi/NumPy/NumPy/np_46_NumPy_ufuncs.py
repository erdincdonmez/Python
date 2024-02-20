# klasik yöntemle dizileri toplama
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print("\nKlasik yöntemle dizileri toplama : \n",z)

# NumPy ile dizileri toplama
import numpy as np
z = np.add(x, y)
print("\nNumPy ile dizileri toplama       : \n",z)

