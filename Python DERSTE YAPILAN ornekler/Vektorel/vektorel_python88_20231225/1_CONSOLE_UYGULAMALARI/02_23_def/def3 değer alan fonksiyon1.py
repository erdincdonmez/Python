# değer alan fonksiyonlar
def selamla():
    print("Merhaba")
    print("Nasılsın")
    
def topla(aa,bb):
    print(aa,"ile",bb,"toplamı:",aa+bb)

def carp(aa,bb):
    print(aa,"ile",bb,"çarpımı:",aa*bb)

def cikar(aa,bb):
    print(aa,"ile",bb,"farkı:",aa-bb)

def bol(aa,bb):
    print(aa,"ile",bb,"bolumu:",aa/bb)

def tamBol(aa,bb):
    print(aa,"ile",bb,"kusuratsız bölümü:",aa//bb)

def ustAl(aa,bb):
    print(aa,"üzeri",bb,"=",aa**bb)

xx = 10
yy = 3
topla(xx,yy)# parametre gönderimi
carp(xx,yy)
carp(xx,2)
bol(xx,yy)
tamBol(xx,yy)
ustAl(xx,yy)
