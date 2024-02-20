# Trigonometric Functions
# sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.
import numpy as np

x = np.sin(np.pi/2)
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

# radians values are pi/180 * degree_values.
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print("deg2rad : ",x)

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print("rad2deg : ",x)

x = np.arcsin(1.0)
print("Finding Angles: ",x)

arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print("Finding Angles: ",x)

base = 3
perp = 4
x = np.hypot(base, perp)
print("Hypotenues",x)

