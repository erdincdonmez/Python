# Verilen bir sayıya kadar olan sayıların toplamını bulan programı recursive fonksiyon ile yapacak olursak
def toplam(x):
    if x == 1:
        return 1
    else:
        return (x + toplam(x-1))
sayi = int(input("Bir sayı giriniz: "))
print(sayi, "sayısına kadar olan sayıların toplamı:", toplam(sayi))
