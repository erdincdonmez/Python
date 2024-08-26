class Ilan():
    aktiflik = True
    def __init__(self, no, bas):
        self.ilanNo = no
        self.baslik = bas
        
    def ilanBilgisi(ddd):
        print("No: ",ddd.ilanNo, "Baslik : ",ddd.baslik)

class Arac(Ilan):
    def __init__(self,no,bs,fy,tur):
        super().__init__(no,bs)
        self.aracFiyati = fy
        self.aracTuru = tur
        
# ilan1148975819 = Ilan(1148975819,"Pıtır pıtır şahin")
# ilan1587458956 = Ilan(1587458956,"Aslanlar gibi toros")

# ilan1148975819.ilanBilgisi()
# ilan1587458956.ilanBilgisi()

arac1 = Arac(1148975819,"Pıtır pıtır şahin",500000,"Binek")
arac1.ilanBilgisi()

class Ev(Ilan):
    def __init__(self, no, bas, m2_, konumu_):
        super().__init__(no, bas)
        self.m2 = m2_
        self.konum = konumu_

class KiralikEv(Ev):
    def __init__(self, no, bas, m2_, konumu_, depozito, kirasi):
        super().__init__(no, bas, m2_, konumu_)
        self.depozito = depozito
        self.kirasi = kirasi

class SatilikEv(Ev):
    def __init__(self, no, bas, m2_, konumu_, fiyati, ipotek):
        super().__init__(no, bas, m2_, konumu_)
        self.fiyat = fiyati
        self.ipotek = ipotek
    def ilanBilgisi(ddd):
        print("No: ",ddd.ilanNo, "Baslik : ",ddd.baslik, "Büyüklüğü:",ddd.m2)

ilan234 = SatilikEv(23652,"Sahibindn kelepir 2+1",120,"Demetevler",1500000,"Yok")
ilan234.ilanBilgisi()
