import os
yer = os.getcwd()
print("YERİMİZ => "+yer)

for a in os.listdir(yer):
    print(a)

yer += "\\cc"
print("YERİMİZ => "+yer)

for a in os.listdir(yer):
    print(a)


"""
yer += "/cc"
os.chdir(yer)
print(os.getcwd())
"""
