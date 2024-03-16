# break continue
for a in range(1,11): 
    # print(a)
    if a == 3 : continue
    for b in range(1,11): 
        print(a,"x",b,"=",a*b)
    print()
    if a == 5 : break