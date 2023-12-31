print("Not hesabı")
sınav_1 = int(input("1.sınav notunuzu girin: "))
sınav_2 = int(input("2.sınav notunuzu girin: "))
ortalama = (sınav_1 + sınav_2)/2

if (sınav_1 > 100 or sınav_1<0) or (sınav_2 > 100 or sınav_2<0):
    print ("Notlar 0 ile 100 arasında olabilir")
else: # Sınav notlarında hata yoksa aşağıdakiler çalışacak
    if ortalama >= 90: print ("Harikasın AA aldın")
    elif ortalama >= 70 : print ("Notun fena değil. BB aldın")
    elif ortalama >= 50 : print ("Geçtin işte",ortalama)
    else:
        print("malesef")
