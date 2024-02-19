# NumPy Data distrubution
from numpy import random
x = random.choice([3, 5], p=[0.2, 0.8], size=(4, 5))
print("\n3 ten 0.2, 5 ten 0.8 oranında kullanarak yeni bir dizi:\n",x)