for a in range(1,11):
    if a == 5 : continue
    if a == 8: break
    for b in range (1,11):
        if b == 5 : continue
        print(a,"x",b,"=",a*b)
        if a == 6: break
    print()
    


