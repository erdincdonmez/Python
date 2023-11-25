import random
print("BİLGİ YARIŞMASINA HOŞ GELDİNİZ.")
print("==========================================\n")
sorular = [
    "Nazendenin kardeşinin adı nedir?",
    "Cek Cumhuriyeyinin başkenti neresidir?",
    "Ankara hangi ülkededir?",
    "Atatürk hangi yılda doğdu?",
    "Pythonu kim üretti?",
    "Almanyanin başkenti neresidir?"
    ]
cevaplar = [
    "Kuzey",
    "Prag",
    "Türkiye",
    "1881",
    "Roussom",
    "Berlin"
    ]
maxpuan = 100
puan = 0
sorusayisi = len(sorular)
sorulacaksorusayisi=5
birsorupuani = maxpuan/sorulacaksorusayisi
print("Her soru",birsorupuani,"dır.")
for n in range(sorulacaksorusayisi):
    #print(random.randint(1,sorusayisi))
    kacinci = random.randint(0,sorusayisi-1)
    cevap = input(sorular[kacinci])
    if cevap == cevaplar[kacinci] :
        print("Doğru bildiniz")
        puan += birsorupuani
    else:
        print("Bilemediniz.")
        puan -= birsorupuani/2
    print("Puaniniz",puan)


    

