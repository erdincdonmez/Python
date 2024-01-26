# sayi1 = int(input("Bir sayı giriniz:"))
# sayi2 = int(input("Bir sayı giriniz:"))
# print ("Toplamı: ",sayi1+sayi2)
# print("Bir hata oluştu.")
try:
    sayi1 = int(input("Bir sayı giriniz:"))
    sayi2 = int(input("Bir sayı giriniz:"))
    print ("Toplamı: ", sayi1+sayi2)
except:
    print("Bir hata oluştu.")
input()