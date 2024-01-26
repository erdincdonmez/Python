# sayi1 = int(input("Bir sayı giriniz:"))
# sayi2 = int(input("Bir sayı giriniz:"))
# print ("Toplamı: ",sayi1+sayi2)
# print("Bir hata oluştu.")

while True:
    
    try:
        sayi1 = int(input("Bir sayı giriniz:"))
        sayi2 = int(input("Bir sayı giriniz:"))
        print ("Toplamı: ", sayi1+sayi2)
        hata = "yok"
        break

    except:
        print("Bir hata oluştu. Yeniden girin:")
    if hata == "yok": break

input()