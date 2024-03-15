# NumPy random 
from numpy import random

x = random.choice([3, 5], p=[0.4, 0.6], size=(10))
print("3 ten 0.4, 5 ten 0.6 oranında kullanarak yeni bir dizi:",x)

x = random.choice([3, 5], p=[0.2, 0.8], size=(3, 5))
print("\n3 ten 0.2, 5 ten 0.8 oranında kullanarak 3x5 yeni bir dizi:\n",x)
