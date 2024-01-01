import sys
from PyQt6.QtWidgets import *
import proje4_moduls.inchCevirici
import proje4_moduls.ogrenciTakip
import mysql.connector

class veritabani():
    veritabaniHost = "localhost"
    veritabaniUser = "root"
    veritabaniPass = "1234"
    veritabaniAdi = "proje3database"
    def __init__(self, host = "localhost", user = "root", passs = "1234", name = "proje3database"):
        self.veritabaniHost = host
        self.veritabaniUser = user
        self.veritabaniPass = passs
        self.veritabaniAdi = name

veritabani1 = veritabani()

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Evrensel Uygulama")
        self.arayuz()

    def arayuz(self):
        ana_widget = QWidget()
        layout = QVBoxLayout()
       
        layout.addWidget(QLabel("Hangi uygulamayı kullanacaksın?"))

        uygulama1 = QPushButton("Inch Çevirici")
        uygulama1.clicked.connect(self.uygulama1Tiklanma)
        layout.addWidget(uygulama1)

        uygulama2 = QPushButton("Öğrenci Takip")
        uygulama2.clicked.connect(self.uygulama2Tiklanma)
        layout.addWidget(uygulama2)

        ana_widget.setLayout(layout)
        self.setCentralWidget(ana_widget)

    def uygulama1Tiklanma(self):
        # self.close()  # Login penceresini kapat
        self.uygulama1 = proje4_moduls.inchCevirici.inchCeviriciWindow()
        self.uygulama1.show()
   
    def uygulama2Tiklanma(self):
        # self.close()  # Login penceresini kapat
        # sys.path.remove('../')
        self.uygulama2 = proje4_moduls.ogrenciTakip.OgrenciTakipPenceresi()
        self.uygulama2.show()

def veritabaniIslemleri(istenenVT):
    import mysql.connector
    veritabaniAdi = istenenVT
    tablo1 = "ogrenciler"
    tablo2 = "ogretmenler"
    tablo3 = "kullanicilar"
    try: # veritabanı bağlantısı yapılıyor..
        baglanti = mysql.connector.connect(
            host= veritabani.veritabaniHost, # Veritabanı sistemi adı (instance).
            user= veritabani.veritabaniUser, # Veritabanı kullanıcı adı
            password= veritabani.veritabaniPass # Veritabanı sistemi(instance) şifresi
        )
        secilenDB = baglanti.cursor()
        # secilenDB.execute(f"SHOW DATABASES LIKE '{veritabaniAdi}'")
        secilenDB.execute(f"SHOW DATABASES")
        veritabaniListesi = secilenDB.fetchall()
        # İstenilen veritabanının var olup olmadığını kontrol etme
        if (f'{veritabaniAdi}',) in veritabaniListesi:
            print(f"{veritabaniAdi} adlı veritabanı mevcut")
            print("Bağlantı tamam:", baglanti)
            
            baglanti = mysql.connector.connect(
                host= veritabani.veritabaniHost, # Veritabanı sistemi adı (instance).
                user= veritabani.veritabaniUser, # Veritabanı kullanıcı adı
                password= veritabani.veritabaniPass, # Veritabanı sistemi(instance) şifresi
                database = veritabani.veritabaniAdi
            )
            secilenDB = baglanti.cursor()
            # secilenDB.execute(f"SHOW TABLES LIKE '{tablo1}'")
            secilenDB.execute(f"SHOW TABLES")
            # Sonucu al
            tabloListesi = secilenDB.fetchall()
            # İstenilen tablonun var olup olmadığını kontrol etme
            if (tablo1,) in tabloListesi:
                print(f"{tablo1} tablosu mevcut")
            else:
                print(f"{tablo1} tablosu mevcut değil")
                secilenDB.execute(f"CREATE TABLE IF NOT EXISTS {tablo1} (id INT, tc VARCHAR(11), adsoyad VARCHAR(50), sinif VARCHAR(30))")
                print(f"{tablo1} tablosu oluşturuldu.")    
            
            if (tablo2,) in tabloListesi:
                print(f"{tablo2} tablosu mevcut")
            else:
                print(f"{tablo2} tablosu mevcut değil")
                secilenDB.execute(f"CREATE TABLE IF NOT EXISTS {tablo2} (id INT, tc VARCHAR(11), adsoyad VARCHAR(50), brans VARCHAR(30))")
                print(f"{tablo2} tablosu oluşturuldu.")    
            if (tablo3,) in tabloListesi:
                print(f"{tablo3} tablosu mevcut")
            else:
                print(f"{tablo3} tablosu mevcut değil")
                secilenDB.execute(f"CREATE TABLE IF NOT EXISTS {tablo3} (id INT, kullaniciadi VARCHAR(50), sifre VARCHAR(30))")
                print(f"{tablo3} tablosu oluşturuldu.")   
                komut = "INSERT INTO kullanicilar (id, kullaniciadi, sifre) VALUES (%s, %s, %s)"
                data = [
                    (1, 'admin', '1234'),
                    (2, 'q','q')
                        ]
                # secilenDB.execute(komut, data)  
                secilenDB.executemany(komut, data)  
                baglanti.commit()
        else:
            print(f"{veritabaniAdi} adlı veritabanı mevcut değil.")
            try: # yoksa veritabanı oluşturuluyor..
                secilenDB.execute(f"CREATE DATABASE IF NOT EXISTS {veritabaniAdi};")
                baglanti = mysql.connector.connect(
                    host= veritabani.veritabaniHost, # Veritabanı sistemi adı (instance).
                    user= veritabani.veritabaniUser, # Veritabanı kullanıcı adı
                    password= veritabani.veritabaniPass, # Veritabanı sistemi(instance) şifresi
                    database = veritabani.veritabaniAdi
                )
                secilenDB = baglanti.cursor()
                print(f"{veritabaniAdi} adlı veritabanı oluşturuldu.")
                secilenDB.execute(f"CREATE TABLE {tablo1} (id INT, tc VARCHAR(11), adsoyad VARCHAR(50), sinif VARCHAR(30))")
                print(f"{tablo1} tablosu oluşturuldu.")
                secilenDB.execute(f"CREATE TABLE {tablo2} (id INT, tc VARCHAR(11), adsoyad VARCHAR(50), brans VARCHAR(30))")
                print(f"{tablo2} tablosu oluşturuldu.")
                secilenDB.execute(f"CREATE TABLE IF NOT EXISTS {tablo3} (id INT, kullaniciadi VARCHAR(50), sifre VARCHAR(30))")
                print(f"{tablo3} tablosu oluşturuldu.")   
                komut = "INSERT INTO kullanicilar (id, kullaniciadi, sifre) VALUES (%s, %s, %s)"
                data = [
                    (1, 'admin', '1234'),
                    (2, 'q','q')
                        ]
                secilenDB.executemany(komut, data)  
                baglanti.commit()
                print("Kullanıcılar oluşturuldu.")
            except mysql.connector.Error as hata:
                print(f"Veri tabanı/tablo oluşturulamadı. Hata : {hata}")
    except mysql.connector.Error as hata:
        print (f"İşlem başarısız. Hata: {hata}")
    finally:
        baglanti.close()

def kullaniciKontrol(istenenVT,kullanici,sifre):
    baglanti = mysql.connector.connect(
        host= veritabani.veritabaniHost, # Veritabanı sistemi adı (instance).
        user= veritabani.veritabaniUser, # Veritabanı kullanıcı adı
        password= veritabani.veritabaniPass, # Veritabanı sistemi(instance) şifresi
        database = istenenVT
        )
    secilenDB = baglanti.cursor()
    secilenDB.execute(f"SELECT * FROM kullanicilar WHERE kullaniciadi = '{kullanici}'")
    alinanVeri = secilenDB.fetchall()
    baglanti.close()
    # print (alinanVeri)
    # print (alinanVeri[0][1])
    if len(alinanVeri) > 0 and kullanici == alinanVeri[0][1] and sifre == alinanVeri[0][2]:
        return True
    else: return False

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Ekranı")
        self.arayuz()
    veritabaniIslemleri(veritabani.veritabaniAdi)
    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        label_username = QLabel("Kullanıcı Adı:")
        self.username_input = QLineEdit()
        layout.addWidget(label_username)
        layout.addWidget(self.username_input)

        label_password = QLabel("Şifre:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(label_password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Giriş Yap")
        login_button.clicked.connect(self.login)
        login_button.setAutoDefault(True)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        sonuc = kullaniciKontrol(veritabani.veritabaniAdi,username,password)
        if sonuc : self.open_AnaEkran()
        else: QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")
        # Kullanıcı adı ve şifreyi kontrol etme - Örnek amaçlı basit bir kontrol
        # if username == "q" and password == "q":
        #     self.open_AnaEkran()
        # else: QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def open_AnaEkran(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
        self.close()  # Login penceresini kapat
        self.anaEkran = AnaPencere()
        self.anaEkran.show()
       
def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()