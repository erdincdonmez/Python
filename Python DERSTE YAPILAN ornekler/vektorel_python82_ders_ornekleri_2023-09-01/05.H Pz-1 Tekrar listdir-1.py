# dosya ve dizinlerin maddeler halindeki, numaralı listesi.
import os
dosyaDizinListesi = os.listdir("D:\\") # mevcut konumdaki dosya ve dizinlerin dizi olarak listesi.
for x in range (len(dosyaDizinListesi)):
    print (x+1," - ",dosyaDizinListesi[x])
