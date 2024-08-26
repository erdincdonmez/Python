class Calisan:
    # __baslangicMaasi = 17500
    def __init__(self,ad,tc, maas):
        self._ad = ad # public / her sınıfa, her yere açık
        self.tc = tc
        self.__baslangicMaasi = maas # private/dışarıdan ulaşılamayan değişken.
        # Sadece kendi sınıfının içindeki metodlar ile ulaşılabilir.
   
    def bilgiYazdir(self):
        print(f"Çalisan adı:{self._ad}, baş.maaşı:{self.__baslangicMaasi}")
    
    def baslangicMaasiArtir(self,yeniMaasi):
        self.__baslangicMaasi = yeniMaasi

calisan1 = Calisan("Murat",698,25000)
calisan2 = Calisan("Dila",741,30000)

calisan2.bilgiYazdir()
calisan2.__baslangicMaasi = 40000
calisan2._ad = "Yasin"
calisan2.bilgiYazdir()
print(calisan2.__baslangicMaasi)