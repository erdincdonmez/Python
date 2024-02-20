class Ilan ():
    IlanNo = 0
    IlanBaslik = ""
    IlanSahibi = ""
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

ilan1 = Ilan(n = 13246, b = "Metroyayakın ev", s = "Eren Korkmaz") # nesne oluşturma
print(ilan1.bilgi1)
# print(ilan1.bilgi())
# ilan1.kaydet()
print(ilan1.IlanNo)
        
        