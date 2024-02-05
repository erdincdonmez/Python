class Ilan ():
    
    def __init__(self, n, b, s, a):
        self.IlanNo = n
        self.IlanBaslik = b
        self.IlanSahibi = s
        self.IlanAciklama = a
    def bilgi(self):
        print("No:", self.IlanNo, "Başlık:", self.IlanBaslik)
        
class Ev(Ilan):
    def __init__(self, n, b, s, a, o,f):
        self.OdaSayisi = o # public / global
        self.__fiyat = f # private
        
    def evFiyatiYaz(self,f):
        self.__fiyat = f/2

    def bilgi(self):
         print("Oda Sayısı:",self.OdaSayisi, self.__fiyat)

class Arac(Ilan):
    AracMarkasi = ""
    def __init__(self, n, b, s, a, m, f):
        self.AracMarkasi = m
        self.__fiyat = f

    def bilgi(self):
        print("Marka:",self.AracMarkasi)

ilan1 = Ilan(13246,"Metroyayakın ev","Eren Korkmaz","Açıklama") # nesne oluşturma
ilan2 = Ev(13246, "Metroyayakın ev", "Mustafa Korkmaz", "Açıklama",3,1000) 
ilan3 = Arac(13246, "Metroyayakın ev", "Mustafa Korkmaz", "açıklama4","Volvo",2000) 

ilan1.bilgi()
ilan2.bilgi()
ilan3.bilgi()

ilan2.OdaSayisi = 4
ilan2.bilgi()

ilan2.OdaSayisi = 5
ilan2.__fiyat = 5000
ilan2.bilgi()
# print("İlan2 odasayısı:",ilan2.OdaSayisi)
# print("İlan2 fiyatı   :",ilan2.__fiyat)
ilan2.evFiyatiYaz(6000)
ilan2.bilgi()

        
