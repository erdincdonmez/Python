def menu():
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║  REHBER UYGULAMASI  ║")
    print("║                     ║")
    print("║  1-Kişi ekle        ║")
    print("║  2-Listele          ║")
    print("║  3-Sil              ║")
    print("║  4-Düzelt           ║")
    print("║                     ║")
    print("║  Seçimiz nedir?     ║")
    print("╚═════════════════════╝")
    # 201 ╔ 187 ╗ 200 ╚  # 188 ╝

    secim = input("")
    if secim=="1":
        listele()
        kisiEkle()
    if secim=="2":
        listele()
        menu()

def kisiEkle():
    dosya = open("rehber.txt","a")
    print("╔════════════════════════════╗")
    print("║  Kişi ekleme               ║")
    print("╚════════════════════════════╝")
    ad = input("Kaydedilecek ad ve soyad :")
    nu = input("Kaydedilecek numara      :")
    veri = {"adi":ad,"num":nu}
    dosya.write(str(veri))
    dosya.close()
    menu()

def listele():
    try:
        dosya = open("rehber.txt","r")
        print("╔════════════════════════════╗")
        print("║  Kayıtlı kişiler           ║")
        print("╚════════════════════════════╝")
        okunan1 = dosya.read()
        print(okunan1)
        print("-------------")
        okunan2 = dosya.readline()
        print(okunan2)
        okunan3 = dosya.readline()
        print(okunan3)
        dosya.close()
    except :
        print("Bir hata oluştu")           
menu()
