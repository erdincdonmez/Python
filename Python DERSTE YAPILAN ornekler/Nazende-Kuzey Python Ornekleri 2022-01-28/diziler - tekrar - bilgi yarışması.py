print("BİLGİ YARIŞMASINA HOŞ GELDİNİZ.")
print("==========================================\n")
sorular = []
cevaplar = []
print("Soru giriş bölümü.")
sorusayisi = int(input("Kaç soru olacak? "))
for k in range(sorusayisi):
    soru = input(str(k+1)+".Soruyu girin:")
    sorular.append(soru)
#print("Sorularınız:")
#print(sorular)
print("Soru girişi tamamlandı.")
print("Cevap giriş bölümü.")
for n in range(sorusayisi):
    cevap = input(str(n+1)+".Sorunun cevabını girin:")
    cevaplar.append(cevap)
print("Cevap girişi tamamlandı.")
