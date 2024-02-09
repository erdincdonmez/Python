# logaritma log, log2 ve log10
# üst almanın tersidir. log10(1000)=3, log2(32)=5 
import numpy as np

print("log2([32])   :",np.log2([32]))
print("log2([1000]) :",np.log10([1000]))

# arr = np.arange(1, 10)
arr = np.array([4,8,16,20,32])
print("\narr        :",arr)
print("log2(arr)  :",np.log2(arr))

arr = np.array([100,200,1000,10000])
print("\narr        :",arr)
print("log10(arr) :",np.log10(arr))

# Doğal logaritma : Doğal logaritma, matematikte e tabanında logaritmayı ifade eder. 
# e, matematikte Euler sayısı olarak bilinen sabittir, yaklaşık olarak 2.71828 değerindedir. 
# Doğal logaritma, e tabanında logaritma almak anlamına gelir. ln(x) şekilde ifade edilir
print("log(arr)   :",np.log([2,2.718295,3,7.3891323]))
print("log(arr)   :",np.log([0, -1 , 2]))

from math import log
xxx = np.frompyfunc(log, 2, 1)
print("frompyfunc :",xxx(16,2)) # 8in log2 si = 3



