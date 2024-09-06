import sys
from PyQt6.QtWidgets import *
import mysql.connector

veritabani = baglanti = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "rehber"
)
secilenVeritabani = veritabani.cursor()

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rehberim")

        central_widget = QWidget()
        layout = QVBoxLayout()

        label_baslik = QLabel("REHBER 1.0")
        layout.addWidget(label_baslik)


        buton_listele = QPushButton("Listele")
        buton_listele.clicked.connect(self.listele)
        layout.addWidget(buton_listele)

        buton_ekle = QPushButton("Ekle")
        buton_ekle.clicked.connect(self.kayitekle)
        layout.addWidget(buton_ekle)

        buton_degistir = QPushButton("Degistir")
        buton_degistir.clicked.connect(self.mesaj)
        layout.addWidget(buton_degistir)


        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))

    def listele(self):
        self.close()  # Login penceresini kapat
        self.listelemeEkrani = ListeEkrani()
        self.listelemeEkrani.show()

    def kayitekle(self):
        self.close()  # Login penceresini kapat
        self.eklemeEkrani = KayitEklemeEkrani()
        self.eklemeEkrani.show()

class ListeEkrani(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rehberim")

        central_widget = QWidget()
        layout = QVBoxLayout()

        label_baslik = QLabel("REHBER LİSTE")
        layout.addWidget(label_baslik)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class KayitEklemeEkrani(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rehberim")

        label_baslik = QLabel("REHBER KAYIT EKLEME")

        icerik6_dikey = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Ad Soyad :"))
        dikeyicerik3.addWidget(QLabel("Telefon  : "))

        dikeyicerik4 = QVBoxLayout()
        self.ad = QLineEdit()
        self.no = QLineEdit()
        dikeyicerik4.addWidget(self.ad)
        dikeyicerik4.addWidget(self.no)
       

        icerik5_yatay = QHBoxLayout()
        icerik5_yatay.addWidget(QPushButton("İptal"))
        kaydetButonu = QPushButton("Kaydet")
        icerik5_yatay.addWidget(kaydetButonu)
        kaydetButonu.clicked.connect(self.kaydet)

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)

        icerik6_dikey.addWidget(label_baslik)
        icerik6_dikey.addLayout(yatayicerik)
        icerik6_dikey.addLayout(icerik5_yatay)

        pencere = QWidget()
        pencere.setLayout(icerik6_dikey)
        self.setCentralWidget(pencere)

    def kaydet(self):
        adi = self.ad.text()
        tel = self.no.text()
        print(f"Kaydedilecek bilgiler: {adi} {tel}")
        secilenVeritabani.execute("CREATE TABLE IF NOT EXISTS veriler (AdiSoyadi VARCHAR(50), Telefonu VARCHAR(30))")
        komut = "INSERT INTO veriler (AdiSoyadi, Telefonu) VALUES (%s, %s)"
        parametreDegerleri = (adi, tel)
        secilenVeritabani.execute(komut, parametreDegerleri)
        veritabani.commit() # cursor ile olanı değil.
        self.ad.setText('')
        self.no.setText('')
        self.ad.setFocus()


def main():
    app = QApplication(sys.argv)
    window = AnaPencere()
    # QMessageBox.information(window, "Cm-Inch Çevirici", "Inch çevirici uygulamasına hoş geldiniz.")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
