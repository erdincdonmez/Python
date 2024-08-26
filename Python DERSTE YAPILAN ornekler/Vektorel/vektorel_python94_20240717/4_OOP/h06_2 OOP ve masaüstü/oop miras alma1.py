class Calisan():
    Odulleri = "" # Sonradan belirleneceği için init içinde değil
    Rutbesi = "" # Sonradan belirleneceği için init içinde değil
    def __init__(self,tc="---",adSoy="---"):
        # if type(tc)==int : print("doğru")
        self.TCKN = tc
        self.AdiSoyadi = adSoy
    def CalisanBilgisi(self):
        print("Çalışan bilgileri: Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN)

# calisan1 = Calisan(adSoy="Erdinç DÖNMEZ",tc="123456")
# calisan1 = Calisan("Erdinç DÖNMEZ","123456")
# calisan1.CalisanBilgisi()

class Idareci(Calisan):
    pass
   
# calisan2 = Calisan("Mustafa Beyazit","654321")
# calisan2.CalisanBilgisi()

calisan3 = Idareci("Ozan CAN","9587458658")
calisan3.CalisanBilgisi()
print(calisan3.AdiSoyadi)
