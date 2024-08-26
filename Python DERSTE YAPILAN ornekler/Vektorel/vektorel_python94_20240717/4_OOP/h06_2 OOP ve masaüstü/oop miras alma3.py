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