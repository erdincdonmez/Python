class Ilan ():
    def __init__(self, n, b, s, a):
        self.IlanNo = n
        self.IlanBaslik = b
        self.IlanSahibi = s
        self.IlanAciklama = a
        
    def bilgi(self):
        print("No:", self.IlanNo, "Başlık:", self.IlanBaslik)

    def kaydet(self):
        d = open("deneme.txt","w")
        kb = f"{self.IlanNo} {self.IlanBaslik} {self.IlanSahibi}\n"
        d.write(kb)
        d.close()
        self.bilgi()

class Ev(Ilan): # miras alma
    def __init__(self, n, b, s, a, o):
        self.OdaSayisi = o
    def bilgi(self):
        print("Oda Sayısı:",self.OdaSayisi)

class Arac(Ilan): # miras alma
    AracMarkasi = ""
    def __init__(self, n, b, s, a, m):
        self.AracMarkasi = m

    def bilgi(self):
        print("Marka:",self.AracMarkasi)

class KiralikEv(Ev):
    def __init__(self, n, b, s, a, o, kf):
        # super.__init__(o)
        self.OdaSayisi = o
        self.kiraFiyati = kf

class SatilikEv():
    pass


ilan1 = Ilan(13246,"Metroyayakın ev","Eren Korkmaz","Açıklama") # nesne oluşturma
ilan2 = Ev(13246, "Metroyayakın ev", "Mustafa Korkmaz", "Açıklama",3) 
ilan3 = Arac(13246, "Metroyayakın ev", "Mustafa Korkmaz", "açıklama4","Volvo") 
ilan4 = KiralikEv(13246, "Metroyayakın ev", "Mustafa Korkmaz", "Açıklama",3,4000) 

ilan1.bilgi()
ilan2.bilgi()
ilan3.bilgi()
ilan4.bilgi()

        
        
