import h02_ct2_hesap_makinesi.hesapmakinesi
import oyunlar.sayi_tahmin_oyunu
import h02_pz2_if.nothesabi
import h03_ct2_for.for04
import h03_pz3_random.random02

def menu():
  #print("\033[1;32;40m")
  print("╔══════════════════════╗")
#  print("║\033[1;31;40m  PYTHON ÇALIŞMALARI\033[1;32;40m  ║")
  print("║  PYTHON ÇALIŞMALARI  ║")
  print("║                      ║")
  print("║ 1-Hesap makinesi     ║")
  print("║ 2-Not hesapla        ║")
  print("║ 3-Sayı tahmin oyunu  ║")
  print("║ 4-Sayma programı     ║")
  print("║ 5-Adam asmaca oyna   ║")
  print("║ 6-Yazı tura oyunu    ║")
  print("║ x-...                ║")
  print("║ x-...                ║")
  print("║ x- Çıkış (e)         ║")
  print("║                      ║")
  print("║    Seçimiz nedir?    ║")
  print("╚══════════════════════╝")
  secim = input()
  print("Seçiniz:", secim)
  if secim == "1": h02_ct_hesap_makinesi.hesapmakinesi.menu()
  if secim == "2":
    h02_pz_if.nothesabi.gectikaldi()
    h02_pz_if.nothesabi.tesekkur_taktir()
    #oyunlar.sayi_tahmin_oyunu.basla()
    menu()
  if secim == "3": adamasmaca.basla()
  if secim == "7" or secim == "e" or secim == "E":
            print("pogramdan çıkılıyor")
            selam.iyiaksamlar()
            exit()
  # import h03_ct2_for.for04
  if secim == "4":
    h03_ct2_for.for04.saydir()
    input("menü için enter'a basın")
    menu()
  if secim =="6":
    h03_pz3_random.random02.sayitahminoyunu()
    menu()
menu()