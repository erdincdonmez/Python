# Bu fonksiyonları çağırırken iki parametre göndermek gerek. Gönderilmese de kendisi atama yapabilir.
# default değerli parametreler sonda tanımlanır
def topla(aa,bb=5): # en az bir parametre gerek
    print(aa,"ile",bb,"toplamı:",aa+bb)

# Bu fonksiyonda parametre gönderilmese de hata vermez
def seriTopla(a=0,b=0,c=0):
    print("Toplam: ",a+b+c)

def carp(a,b=1): print(a,"x",b,"=",a*b)

xx = 10
yy = 3
topla(20,6)
topla(20)# bir parametre olsa da çalışır
seriTopla()
seriTopla(3)
seriTopla(3,4)
seriTopla(2,6,3)
# seriTopla(6,5,2,8) # 4 parametre olmaz
carp(xx,yy)
carp(xx,2)
carp(xx) # bir parametre olsa da çalışır 

import dirhelp
help(dirhelp.deneme)