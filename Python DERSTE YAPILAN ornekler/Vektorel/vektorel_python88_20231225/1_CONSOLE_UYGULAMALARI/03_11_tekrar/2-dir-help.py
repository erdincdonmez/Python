import random
print(round(random.random ()*100))
print(random.randint(1,100))

print(dir(random))
help(random.shuffle)


for i in dir(random):
    print(i)

print(random.choice(dir(random)))
