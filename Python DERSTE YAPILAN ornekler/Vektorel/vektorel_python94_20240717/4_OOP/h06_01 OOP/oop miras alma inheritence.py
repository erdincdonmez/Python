class ilan():
    aktiflik = True
    def __init__(self, no, bas):
        self.ilanNo = no
        self.baslik = bas
        
    def ilanBilgisi(self):
        print("No: ",self.ilanNo, "Baslik : ",self.baslik)


ilan1148975819 = ilan(1148975819,"Pıtır pıtır şahin")
ilan1587458956 = ilan(1587458956,"Aslanlar gibi toros")

ilan1148975819.ilanBilgisi()
ilan1587458956.ilanBilgisi()
