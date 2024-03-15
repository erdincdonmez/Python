# Rounding Decimals
import numpy as np

arr = np.trunc([-3.1666, 3.6667])
print("trunc ile kesme :",arr)

arr = np.fix([-3.1666, 3.6667])
print("fix() ile kesme :",arr)

arr=np.around(3.454, 2)#2 ondaklık sayısı
print("around ile yukarı yuvarlama :",arr)
arr=np.around(3.455, 2)
print("around ile yukarı yuvarlama :",arr)
arr=np.around(3.46, 1)
print("around ile yukarı yuvarlama :",arr)

arr = np.floor([-3.1666, 3.6667])
print("flor ile aşağı yuvarlama",arr)

arr = np.ceil([-3.1666, 3.6667])
print("ceil ile enyakın üst tam sayı :",arr)

