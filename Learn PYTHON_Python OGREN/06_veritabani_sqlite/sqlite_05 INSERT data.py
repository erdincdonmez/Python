# INSERT INTO
import sqlite3
veriTabanı = sqlite3.connect('okultakipsistemi.txt') # varsa bağlan, yoksa oluştur.
secilenvt = veriTabanı.cursor()

def tabloOlustur():
    secilenvt.execute("CREATE TABLE IF NOT EXISTS ogrenciler(adSoyad TEXT, numara INT) ")
    veriTabanı.commit()

def veriEkle():
    secilenvt.execute("INSERT INTO ogrenciler VALUES('Ali AK','05326589654')")
    veriTabanı.commit()

tabloOlustur()
veriEkle()
veriTabanı.close()
