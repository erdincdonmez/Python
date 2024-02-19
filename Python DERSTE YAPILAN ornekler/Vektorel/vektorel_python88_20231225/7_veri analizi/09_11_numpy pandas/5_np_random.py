from numpy import random # NumPy random

# x1 = random.randint(100)
# print("0-100 arası rastgele bir tamsayı   :",x1)

# x2 = random.rand()
# print("0 ile 1 arasında rastgele bir sayı :",x2)

x3=random.randint(5, size=(5))
print("5 elemanlı bir dizi :",x3)

x4 = random.randint(5, size=(3, 5))
print("\n15 elemanlı 2D(3x5) dizi :\n",x4)