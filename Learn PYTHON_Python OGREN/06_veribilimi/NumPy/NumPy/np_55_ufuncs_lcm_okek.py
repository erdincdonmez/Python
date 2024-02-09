# lcm veya okek/ekok
import numpy as np

num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)

arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)

