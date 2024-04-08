# IF NOT EXISTS
import sqlite3
veriTabanı = sqlite3.connect('okultakipsistemi.txt') # varsa bağlan, yoksa oluştur.
secilenvt = veriTabanı.cursor()

def tabloOlustur():
    secilenvt.execute("CREATE TABLE IF NOT EXISTS ogrenciler(adSoyad TEXT, numara INT) ")
    veriTabanı.commit()
    veriTabanı.close()

tabloOlustur()