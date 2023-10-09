def topla():
    print("TOPLAMA İŞLEMİ")
    print("Toplamı:",sayi1+sayi2)
def cikar():
    print("ÇIKARMA İŞLEMİ")
    print("Farkı  :",sayi1-sayi2)


konu = "HESAP MAKİNESİ"
print("\033[1;33;40m") # renkli yazmak için yaptık
print("╔"+"═"*(len(konu)+2)+"╗")
print("║ \033[1;31;40m"+konu+"\033[1;33;40m ║")
print("╠"+"═"*(len(konu)+2)+"╣")
# print("╚ ╝") print("\033[1;31;40m")
print("║ \033[1;31;40m 1-TOPLAMA    \033[1;33;40m ║")
print("║ \033[1;31;40m 2-ÇIKARMA    \033[1;33;40m ║")
print("║ \033[1;31;40m 3-ÇARPMA     \033[1;33;40m ║")
print("║ \033[1;31;40m 4-BÖLME      \033[1;33;40m ║")
print("║ \033[1;31;40m 5-ÇIKIŞ      \033[1;33;40m ║")
print("╚"+"═"*(len(konu)+2)+"╝")

sayi1 = int(input("\033[1;34;40m1.sayıyı giriniz: \033[1;35;40m"))
sayi2 = int(input("\033[1;34;40m2.sayıyı giriniz: \033[1;35;40m"))

secim = input("\033[1;31;40mİşleminiz hangisi(1-4)? ")

if secim == "1": topla()
    
if sayi2>sayi1:
    gecici = sayi2
    sayi2 = sayi1
    sayi1 = gecici 

if secim == "2": cikar()
    
if secim == "3": 
    print("ÇARPMA İŞLEMİ")
    print("Çarpımı:",sayi1*sayi2)
if secim == "4": 
    print("Bölümü :",sayi1/sayi2)
if secim == "5": exit()



print("\033[1;37;40m")
input()