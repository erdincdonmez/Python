
class Calisan():
    Odulleri = "" # Sonradan belirleneceği için init içinde değil
    Rutbesi = "" # Sonradan belirleneceği için init içinde değil
    
    def __init__(self,tc="---",adSoy="---"):
        self.TCKN = tc
        self.AdiSoyadi = adSoy

    def CalisanBilgisi(self):
        print("Çalışan bilgileri: Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN)

calisan1 = Calisan("Erdinç DÖNMEZ","123456")
calisan1.CalisanBilgisi()

class Idareci(Calisan):
    pass

class Ogretmen(Calisan):
    pass
   
calisan2 = Calisan("Mustafa Beyazit","654321")
calisan2.CalisanBilgisi()

calisan3 = Idareci()
calisan3.CalisanBilgisi()

calisan3 = Idareci("","Oğuzhan AKGÜN")
calisan3.CalisanBilgisi()
