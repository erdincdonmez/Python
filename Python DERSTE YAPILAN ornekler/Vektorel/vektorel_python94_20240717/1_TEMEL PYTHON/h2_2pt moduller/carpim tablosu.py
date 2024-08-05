# çarpım tablosu
for a in range(1,11):
    # print(a)
    if a == 2: continue
    for b in range(1,11):
        if b > 8 : continue
        print(a,"x",b,"=",a*b)
        if b == 5: break
    print()
    if a == 7: break