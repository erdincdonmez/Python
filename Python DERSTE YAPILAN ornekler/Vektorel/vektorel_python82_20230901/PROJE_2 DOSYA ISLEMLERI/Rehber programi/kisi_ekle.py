def ekle():
    dosya = open("rehber.txt","a")
    ad      = input("Adı      : ")
    soyad   = input("Soyadı   : ")
    telefon = input("Telefonu : ")
    dosyayaYazilacak = ad +" "+ soyad +" "+ telefon+"\n"
    dosya.writelines(dosyayaYazilacak)
    dosya.close()
