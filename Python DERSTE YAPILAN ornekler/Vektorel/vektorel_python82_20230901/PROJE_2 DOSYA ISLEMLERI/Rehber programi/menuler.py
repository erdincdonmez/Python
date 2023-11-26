import listele
# import kayitmodulu
import kisi_ekle

rehberIsimleri=[]

def anaMenu():
    secim = ""
    while secim!="x":
        print("\n\nREHBER PROGRAMI")
        print("===============")
        print("1-Rehbere ekleme")
        print("2-Rehberi listeleme")
        print("x-Çıkış")
        secim = input("Seçiminiz:")
        if secim == "1": kisi_ekle.ekle()
        if secim == "2": listelemeMenusu()
    print("Çıkış yapıldı.")
    
def listelemeMenusu():
    print("\nLİSTELEME MENÜSÜ")
    print("================")
    print("1-Listele")
    print("2-Ada göre listele")
    print("X-Anamenüye dön")
    secim = input("Seçiminiz:")
    if secim == "1":
        listele.duzListele()
    if secim == "2":
        listele.siraliListele()
    if secim.lower() == "x": anaMenu()
    

