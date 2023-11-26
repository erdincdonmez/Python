class Ogrenci:
    TC = "123"
    adi ="Alper"
    soyadi = "ŞAHİN"
    def OgrenmeneBilgi(self):
        print ("Öğrenci bilgisi: Adı:",self.ad,"Soyadı:",self.soyad)

    def IdareciyeBilgi(self):
        print ("Öğrenci bilgisi: TC:",self.TC,"Adı:",self.Adi,"Soyadı:",self.soyad)

##ogrenci1 = Ogrenci(TC="123",adi="Arda")
ogrenci1 = Ogrenci()

##print(ogrenci1.OgrenmeneBilgi)
print(ogrenci1.TC)
##print(Ogrenci.__dict__)



##ogrenci = Ogrenci(TC="123",Adi="Arda")
##
##print(ogrenci.TC)
