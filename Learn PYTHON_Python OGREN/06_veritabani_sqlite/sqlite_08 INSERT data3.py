# INSERT INTO
import sqlite3
veriTabanı = sqlite3.connect('okultakipsistemi.db') # varsa bağlan, yoksa oluştur.
secilenvt = veriTabanı.cursor()

def tabloOlustur():
    secilenvt.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT, sinif TEXT) ")
    veriTabanı.commit()

def veriEkle(*gelen):
    # print(gelen[0],gelen[1],gelen[2])
    # secilenvt.execute(f"INSERT INTO {gelen[0]} VALUES ('{gelen[1]}', '{gelen[2]}')")
    secilenvt.execute(f"INSERT INTO {gelen[0]}(ad, sinif) VALUES (?,?)",(gelen[1], gelen[2]))
    veriTabanı.commit()

def kayitEkleme():
    adi    = input("Öğrenci adı   : ")
    sinifi = input("Öğrenci sınıfı: ")
    veriEkle("ogrenciler",adi,sinifi)

tabloOlustur()
kayitEkleme()
veriTabanı.close()
