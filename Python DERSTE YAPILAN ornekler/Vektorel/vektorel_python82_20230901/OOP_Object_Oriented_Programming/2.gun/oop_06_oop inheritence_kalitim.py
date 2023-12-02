class Ilan():
    ilanNo=""
    ilanTarihi=""

class Arac(Ilan):
    turu=""
    fiyat=0

class Emlak(Ilan):
    turu=""
    mk = 0

class Konut(Emlak):
    katSayisi=""
    imarDurumu=""

class KiralikEv(Konut):
    kiraMiktari = 0

ilan1 = KiralikEv
ilan1.ilanNo = "123"

print (ilan1.ilanNo)
    
    
        
