class Ilan ():
    IlanNo = 0
    IlanBaslik = ""
    IlanSahibi = ""
    IlanAciklama = ""
    
    def __init__(self, n, b, s):
        self.IlanNo = n
        self.IlanBaslik = b
        self.IlanSahibi = s
        
    def bilgi(self):
        print("No:", self.IlanNo, "Başlık:", self.IlanBaslik)

    def bilgi1(self):
        return "No:"+ self.IlanNo+ "Başlık:"+ self.IlanBaslik

    def kaydet(self):
        d = open("deneme.txt","w")
        kb = f"{self.IlanNo} {self.IlanBaslik} {self.IlanSahibi}\n"
        d.write(kb)
        d.close()
        self.bilgi()

class Ev():
    IlanNo = 0
    IlanBaslik = ""
    IlanSahibi = ""
    IlanAciklama = ""
    OdaSayisi = 0
    def __init__(self, n, b, s, o):
        self.IlanNo = n
        self.IlanBaslik = b
        self.IlanSahibi = s
        self.OdaSayisi = o
    def bilgi(self):
        print("No:", self.IlanNo, "Başlık:", self.IlanBaslik, "Oda Sayısı:",self.OdaSayisi)

class Arac():
    IlanNo = 0
    IlanBaslik = ""
    IlanSahibi = ""
    IlanAciklama = ""
    AracMarkasi = ""
    def __init__(self, n, b, s, m):
        self.IlanNo = n
        self.IlanBaslik = b
        self.IlanSahibi = s
        self.AracMarkasi = m
    def bilgi(self):
        print("No:", self.IlanNo, "Başlık:", self.IlanBaslik, "Marka:",self.AracMarkasi)

ilan1 = Ilan(n = 13246, b = "Metroyayakın ev", s = "Eren Korkmaz") # nesne oluşturma
ilan2 = Ev(n = 13246, b = "Metroyayakın ev", s = "Mustafa Korkmaz", o=3) 
ilan3 = Arac(n = 13246, b = "Metroyayakın ev", s = "Mustafa Korkmaz", m="Volvo") 
# print(ilan1.bilgi1)
ilan1.bilgi()
ilan2.bilgi()
ilan3.bilgi()
# print(ilan1.bilgi())
# ilan1.kaydet()
# print(ilan1.IlanNo)
        
        