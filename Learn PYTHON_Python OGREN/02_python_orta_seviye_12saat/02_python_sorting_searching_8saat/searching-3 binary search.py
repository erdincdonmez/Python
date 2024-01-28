def bolAra(aranacakyer, deger):
    ilk = 0
    elemansayisi = len(aranacakyer)
    yer = -1
    while (ilk <= elemansayisi) and (yer == -1):
        orta = (ilk+elemansayisi)//2
        if aranacakyer[orta] == deger:
            yer = orta
        else:
            if deger<aranacakyer[orta]:
                elemansayisi = orta -1
            else:
                ilk = orta +1
    return yer

sayilar = [10,20,30,40,50]
print(bolAra(sayilar,50))
