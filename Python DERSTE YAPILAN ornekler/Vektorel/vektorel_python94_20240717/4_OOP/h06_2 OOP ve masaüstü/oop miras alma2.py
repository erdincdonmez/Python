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
    EkUcret = 0 # Sonradan belirleneceği için init içinde değil
    def __init__(self,tc="---",adSoy="---",grv="Henüz hanımlı değil"):
        super().__init__(tc,adSoy)
        self.Gorev = grv
    def CalisanBilgisi(self): # Miras aldığı metodu override ettik. Üzerine yazdık.
        print("Yonetici bilgileri: Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN," Görevi:",self.Gorev)
   
calisan2 = Calisan("Mustafa Beyazit","654321")
calisan2.CalisanBilgisi()

# calisan3 = Idareci()
# calisan3.CalisanBilgisi()

calisan4 = Idareci("Mehmet ARLI","215463","Müdür")
calisan4.CalisanBilgisi()
