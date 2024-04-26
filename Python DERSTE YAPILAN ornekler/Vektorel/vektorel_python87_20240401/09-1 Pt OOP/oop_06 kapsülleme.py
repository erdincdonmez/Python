class Ogrenci:
    def __init__(self,xx,yy,zz="Normal"): 
        self._ad = xx # public / her sınıfa, her yere açık
        self.no = yy
        self.__sd = zz # private/dışarıdan ulaşılamayan değişken.
        # Sadece kendi sınıfının içindeki metodlar ile ulaşılabilir.
    
    def saglikDurumu(self):
        return self.__sd

ogrenci1 = Ogrenci("Murat",698)
ogrenci2 = Ogrenci("Dila",741,"Astımı var") # Nesneye veri set etme
print(ogrenci2.__sd)
print(ogrenci1._ad)
# print(ogrenci1.__sd)
print(ogrenci1.saglikDurumu())
print(ogrenci2.saglikDurumu()) # sd (sağlık durumu) nu okumak için method kullan.
# ogrenci1.__sd = "xxx"
# print(ogrenci1.__sd)
# print(ogrenci1.saglikDurumu())