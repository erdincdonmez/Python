# import listele
# import kayitmodulu

rehberIsimleri=[]

def anaMenu():
    print("REHBER PROGRAMI")
    print("===============")
    print("1-Rehbere ekleme")
    print("2-Rehberi listeleme")
    secim = input("Seçiminiz:")
    if secim == "1":        
        eklenecek = input("Rehbere eklenecek isim nedir? ")
        rehbereEkle(eklenecek)
    if secim == "2": listelemeMenusu()
    
def listelemeMenusu():
    print("LİSTELEME MENÜSÜ")
    print("================")
    print("1-Listele")
    print("2-Ada göre listele")
    print("X-Anamenüye dön")
    secim = input("Seçiminiz:")
    if secim == "1": duzListele()
    if secim == "2": siraliListele()
    if secim.lower() == "x": anaMenu()
    
def rehbereEkle(eklenecekAd):
    rehberIsimleri.insert(len(rehberIsimleri),eklenecekAd)
    duzListele()

def duzListele():
    print("REHBERDEKİLER (SIRASIZ)")
    print("======================")
    
    for a in rehberIsimleri:
        print(a)
    anaMenu()

def siraliListele():
    print("REHBERDEKİLER (SIRALI)")
    print("======================")
    rehberIsimleri.sort()
    for a in rehberIsimleri:
        print(a)
    anaMenu()
    
