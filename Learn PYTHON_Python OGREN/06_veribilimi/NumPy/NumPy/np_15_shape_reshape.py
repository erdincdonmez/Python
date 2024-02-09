# SHAPE
import numpy as np
a1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a1.shape)
a2 = np.array([1, 2, 3, 4], ndmin=5)
print(a2)
print('shape of array :', a2.shape)

# reshape ile diziyi yeniden şekillendirebiliriz.
# reshape ile çevirimde öge sayısı tam olmazsa hata verir.
a3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newa3 = a3.reshape(4, 3) # tek boyuttan iki boyuta çevirim.
print("\n\nİki boyutlu anewa4 dizisi:\n",newa3)

newa4 = a3.reshape(2, 3, 2) # Bir boyutluyu 3 boyutlu yapma
print("\n\nÜç boyutlu anewa4 dizisi:\n",newa4)

a5 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("reshape ile düzenlenmiş dizi :",a5.reshape(2, 4))
print("reshape ile düzenlenmiş dizinin base i", a5.reshape(2, 4).base)

a6 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newa6 = a6.reshape(2, 2, -1) # 2,2,2 olması gerekirken bir azaltıyor.
print("\n\nnewa6 :\n",newa6)

a7 = np.array([[1, 2, 3], [4, 5, 6]])
newa7 = a7.reshape(-1) # Bir boyut azaltır.
print("\n\nnewa7 :\n",newa7)