# Ayrık farkı bulmak için diff() kullan
import numpy as np

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)
newarr = np.diff(arr, n=2)
print(newarr)
# İlk dereceden farklar: [15-10, 25-15, 5-25] -> [5, 10, -20]
# İkinci dereceden farklar: [10-5, 15-10, -20-5] -> [5, 5, -25] 
