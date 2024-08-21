# def fonksiyon1(a, b, c, *dd, *ff, **ee): # aynı fonksiyonda iki tane *args veya **kwargs olmaz.
def fonksiyon1(a, b, c, *dd, **ee):
    print(a)
    print(b)
    print(c)
    print(dd)
    print(ee)

fonksiyon1(4,2,4,1,3,5,1,  key1='ankara', sayi=5, key2='izmir')
