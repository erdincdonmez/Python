def anamenu():
    print ("===  WOREX     ===")
    print ("= 1-Hesaplamalar =")
    print ("= 2-Çizimler     =")
    print ("= 3-Yılan oyunu  =")
    print ("= 8-Hesaplamalar =")
    print ("= 9-Çıkış        =")
    print ("==================")
    print ("Seçiminiz nedir?")
    secim = input()
    if secim == "1":
        pass
    if secim == "2":
        import cizimler.cizimlerm
        cizimler.cizimlerm.cizimmenu()
        anamenu()
    if secim == "3":
        import oyunlar.yilan
        oyunlar.yilan.basla()
        anamenu()
        
anamenu()