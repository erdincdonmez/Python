# Dizi elemanlarını okuma.
import numpy as np
# Tek boyutlu dizilerde erişim
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print(arr[2] + arr[3])

# 2 boyutlu dizilerde (matrix) erişim
abc = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('1.Satırın 2.elemanı: ', abc[0, 1])
print('2.Satırın 5.elemanı: ', abc[1, 4])

# 3 boyutlu dizilerde (matrix) erişim
arrx = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("1.Boyutun, 2.Boyutunun, 3.Elemanı",arrx[0, 1, 2])