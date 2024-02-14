from PyQt6.QtWidgets import *
import mysql.connector

app = QApplication([])

class Login(QMainWindow):
    def tiklama1(self):

        # print("Tiklandı")
        kullanici = self.ka.text() 
        sifre     = self.sf.text() 

        # VERİ TABANI İŞLEMLERİ
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="OKULVT"
            )
            print("Bağlandı.")
        except:
            print("Bağlantı hatası.")
        mycursor = mydb.cursor()
        k1 = "SELECT * FROM kullanicilar WHERE kullanici=%s"
        k2 = (kullanici,)
        mycursor.execute(k1,k2)
        gelenBilgi = mycursor.fetchone()
        # print("Kullanici:",kullanici)
        # print("Gelen bilgi:",gelenBilgi)
        # print("Gelen sifre:",gelenBilgi[1])
        
        # mycursor = mydb.cursor()
        # sql = "SELECT * FROM ogrenciler WHERE ad = %s"
        # aranan = ("Esma SARI",)


        # VERİ TABANI İŞLEMLERİ

        # dogruKa = "q"
        # dogruSf = "q"
        dogruKa = kullanici
        dogruSf = gelenBilgi[1]
        mesaj = QMessageBox()
        # mesaj.setText("Tıklandı")
        # mesaj.setText(f"Kullanıcı adı:{kullanici}, Şifre:{sifre}")
        if kullanici == dogruKa and sifre == dogruSf:
            # mesaj.setText("Programa girebilirsin.")
            self.close()  # Login penceresini kapat
            self.xx = AnaEkran()
            self.xx.show()
        else:
            mesaj.setText("Yetki yok.")
            mesaj.exec()

    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı:"))
        self.ka = QLineEdit()
        icerik.addWidget(self.ka)
        icerik.addWidget(QLabel("Şifre:"))
        self.sf = QLineEdit()
        self.sf.setEchoMode(QLineEdit.EchoMode.Password)
        
        icerik.addWidget(self.sf)
        bt = QPushButton("Giriş yap")
        icerik.addWidget(bt)

        bt.clicked.connect(self.tiklama1)

        pencere = QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)

class AnaEkran(QMainWindow):
    def tiklama1(self):
        # mesaj = QMessageBox()
        # mesaj.setText("Uygulama1")
        # mesaj.exec()
        # self.close()
        self.u1 = Uygulama1()
        self.u1.show()
    
    def tiklama2(self):
        mesaj = QMessageBox()
        mesaj.setText("Uygulama2")
        mesaj.exec()

    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("MASAÜSTÜ UYGULAMAMIZA HOŞ GELDİNİZ"))
        bt1 = QPushButton("Uygulama-1")
        icerik.addWidget(bt1)
        bt2 = QPushButton("Uygulama-2")
        icerik.addWidget(bt2)

        bt1.clicked.connect(self.tiklama1)
        bt2.clicked.connect(self.tiklama2)

        pencere = QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)
class Uygulama1(QMainWindow):
    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çeviri programı"))
        le1 = QLineEdit()
        icerik.addWidget(le1)
        bt2 = QPushButton("Çevir")
        icerik.addWidget(bt2)
        le2 = QLineEdit()
        icerik.addWidget(le2)

        pencere = QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)

ekran = Login()
ekran.show()
app.exec()