# Boyut-Dimention 
# 0 Boyutlu Dizi (0-D Arrays)
import numpy as np
arr = np.array(35)
print("1.dizi: ",arr)

# 1 Boyutlu Dizi (1-D Arrays)
import numpy as np
arr1 = np.array([33, 34, 35, 36])
print("tek boyutlu dizi:", arr1)

# 2 Boyutlu Dizi ya da matrix (2-D Arrays )
# Matrix işlemleri için numpy.mat alt modülü kullanılır
import numpy as np
arr2 = np.array([[33,30,35], [4,5,6]])
print("İki boyutlu dizi: ",arr2)

# 2 Boyutlu Dizi ya da matrix (2-D Arrays )
import numpy as np
xxx = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print("3 boyutlu dizi: ",xxx)

# Dizilerin kaç boyutlu olduğunu öğrenelim.
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(xxx.ndim)