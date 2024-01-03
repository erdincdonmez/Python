# değer döndüren fonksiyonlar
def selamla():
    print("Merhaba")
    print("Nasılsın")
    
def topla(aa,bb):
    print(aa,"ile",bb,"toplamı:",aa+bb)
    return aa+bb

def carp(aa,bb):
    # print(aa,"ile",bb,"çarpımı:",aa*bb)
    return aa*bb

def cikar(aa,bb):
    print(aa,"ile",bb,"farkı:",aa-bb)
    return aa-bb

def bol(aa,bb):
    print(aa,"ile",bb,"bolumu:",aa/bb)
    return aa/bb

xx = 10
yy = 3
c = 2
topla(carp(c,xx),yy)# parametre gönderimi
print(carp(xx,yy))
carp(xx,2)
bol(xx,yy)
