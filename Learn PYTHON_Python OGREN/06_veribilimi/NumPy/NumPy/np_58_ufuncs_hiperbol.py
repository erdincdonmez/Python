# Hyperbolic Functions
# NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..
import numpy as np

x = np.sinh(np.pi/2)
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)

x = np.arcsinh(1.0)
print("Finding Angles: ",x)

arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)


