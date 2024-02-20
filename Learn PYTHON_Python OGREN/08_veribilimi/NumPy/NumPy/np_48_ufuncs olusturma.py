# ufunc oluşturma
import numpy as np

def topla(x, y): return x+y

topla = np.frompyfunc(topla, 2, 1)
# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.
print(topla([1, 2, 3, 4], [5, 6, 7, 8]))

print("a function is a ufunc type(np.add)         :",type(np.add))

print("a function is a ufunc type(np.concatenate) :",type(np.concatenate))
#print("a function is a ufunc type(np.abcd):",type(np.abcd)) # hata verir

if type(np.add) == np.ufunc: print('add fonksiyonu bir ufunc tur')
else: print('add fonksiyonu ufunc değildir')