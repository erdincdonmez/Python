def menu():
  print("\033[1;32;40m")
  #print("╔"+"═"*20+"╗")
  print("╔═════════════════════╗")
  print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
  print("║                     ║")
  print("║ 1-Toplama           ║")
  print("║ 2-Çıkarma           ║")
  print("║ 3-Çarpma            ║")
  print("║ 4-Bölme             ║")
  print("║ 5-Üs alma           ║")
  print("║ 6-Kare alan hesabı  ║")
  print("║ 7-Karenin çevresi   ║")
  print("║ 8-Çıkış             ║")
  print("║                     ║")
  print("║    Seçimiz nedir?   ║")
  print("╚═════════════════════╝")
  secim = input()

  print("Seçiniz:", secim)
  if secim == "1": topla()
  if secim == "2": cikar()
  if secim == "3":
    print("Çarpmayı seçtiniz")
  if secim == "4":
    print("Bölmeyi seçtiniz")
  if secim == "5":
    print("Üs alacaksınız")
  if secim == "6":
    print("Kare alan hesabı")
  if secim == "7":
    print("Kare çevresi hesaplaması")
  if secim == "7":
    print("Ana ekrana çıkılıyor")
    exit()


  # 201 ╔
  # 205 ═
  # 187 ╗
  # 186 ║
  # 200 ╚
  # 188 ╝
#def merhabaDe():
#  print("Merhaba")
#  print("nasılsın")


#def sayiTahminOyunu():
#  print("Sayı tahmin oyunu")
#  anaMenu()


#anaMenu()

def topla():
    print("\033[1;31;40mToplamayı seçtiniz\033[1;32;40m")
    sayi1 = int(input("1.Sayıyı giriniz: "))
    sayi2 = int(input("2.Sayıyı giriniz: "))
    print("Toplam:", sayi1 + sayi2)

def cikar():
    print("Çıkarmayı seçtiniz")
    sayi1 = input("1.Sayıyı giriniz: ")
    sayi2 = input("2.Sayıyı giriniz: ")
    print("Farkı :", int(sayi1) - int(sayi2))

