# INSERT INTO
import sqlite3
veriTabani = sqlite3.connect('okultakipsistemi.db') # varsa bağlan, yoksa oluştur.
secilenvt = veriTabani.cursor()

def tabloOlustur():
    secilenvt.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT, sinif TEXT) ")
    veriTabani.commit()

def veriEkle(*gelen):
    # print(gelen[0],gelen[1],gelen[2])
    # secilenvt.execute(f"INSERT INTO {gelen[0]} VALUES ('{gelen[1]}', '{gelen[2]}')")
    secilenvt.execute(f"INSERT INTO {gelen[0]}(ad, sinif) VALUES (?,?)",(gelen[1], gelen[2]))
    veriTabani.commit()

def cokluEkleme():
    komut = 'INSERT INTO ogrenciler VALUES (?, ?)'
    veriler = [
        ('Erhan KARA', '05425236587'),
        ('Burak MERT', '05325214587'),
        ('Alper TOY', '05364125896'),
        ('Ensar GÜL', '05415236541'),
        ('Irmak SAKA', '05426324156'),
        ('Aydın AKA', '05336254158'),
        ('Enes BOZ',  '05465287412'),
        ('Eren SOLAK',  '05075368541'),
        ('Halil Cem AK', '05326325412'),
        ('Yiğit GÜLLÜ',  '05336335241'),
        ('Berkay ÜNLÜ', '05236982544'),
        ('Esma SARI',   '05085236541'),
        ('Arda DOĞRU',   '05436589562'),
        ('Ahmet YOLCU',  '05095236521')
    ]
    secilenvt.executemany(komut, veriler)
    veriTabani.commit()

def kayitEkleme():
    adi    = input("Öğrenci adı   : ")
    sinifi = input("Öğrenci sınıfı: ")
    veriEkle("ogrenciler",adi,sinifi)

tabloOlustur()
# kayitEkleme()
cokluEkleme()
veriTabani.close()
