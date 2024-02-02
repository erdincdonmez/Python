class Anne():
    para : 100000
    ev : 2
    def __init__(self, p = 400000, e=1):
        self.para = p
        self.ev = e

class Baba():
    araba : 2
    arsa : 1
    def __init__(self, a=2, b=1):
        self.araba = a
        self.arsa = b

class Cocuk(Anne):
    bisiklet : 2
    def __init__(self,b,a,z):
        super().__init__(a,z)
        self.bisiklet = b

kisi1 = Cocuk(3,1,5)

print("Cocuğun bisikletleri: ",kisi1.bisiklet)
print("Cocuğun evi: ", kisi1.ev)


