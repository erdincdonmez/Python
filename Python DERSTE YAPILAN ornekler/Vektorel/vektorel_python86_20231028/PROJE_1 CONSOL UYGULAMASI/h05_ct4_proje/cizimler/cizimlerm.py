def cizimmenu():
    print ("===  WOREX-ÇİZİM ===")
    print ("= 1-Kare           =")
    print ("= 2-Üçgen          =")
    print ("= 3-Desen          =")
    print ("= 8-Hesaplamalar   =")
    print ("= 9-Çıkış          =")
    print ("==================")
    print ("Seçiminiz nedir?")
    secim = input()
    if secim == "1":
        pass
    if secim == "2":pass
    if secim == "3":
        import cizimler.desen
        cizimler.desen.desenciz()

    