from PyQt6.QtWidgets import *

class AnaPencere(QWidget): # !!! QWidget olmasına dikkat et !!!
    aktifSayfa = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle("stackedLayout")
   
        anaYerlesim = QVBoxLayout()
        self.stackedSekmeler = QStackedLayout()
        self.setLayout(anaYerlesim)
       
        self.verticalicerik1Butonlar = QHBoxLayout()
        self.buton1 = QPushButton('Öğrenciler')
        self.verticalicerik1Butonlar.addWidget(self.buton1)
        self.buton2 = QPushButton('Öğretmenler')
        self.verticalicerik1Butonlar.addWidget(self.buton2)
        self.buton3 = QPushButton('Ayarlar')
        self.verticalicerik1Butonlar.addWidget(self.buton3)
        self.buton1.clicked.connect(lambda: self.sayfaSec(0)) # lambda ile kullan
        self.buton2.clicked.connect(lambda: self.sayfaSec(1))
        self.buton3.clicked.connect(lambda: self.sayfaSec(2))
       
        self.ogrenciSayfasi = QWidget()
        self.verticalicerik1Ogrenci = QVBoxLayout()
        self.verticalicerik1Ogrenci.addWidget(QLabel('Öğrenci bilgi1'))
        self.verticalicerik1Ogrenci.addWidget(QLabel('Öğrenci bilgi2'))
        self.verticalicerik1Ogrenci.addWidget(QLabel('Öğrenci bilgi3'))
        self.ogrenciSayfasi.setLayout(self.verticalicerik1Ogrenci)
        self.ogrenciSayfasi.setStyleSheet("background-color: gray;")
        self.stackedSekmeler.addWidget(self.ogrenciSayfasi)

        self.ogretmenSayfasi = QWidget()
        self.verticalicerik1Ogretmen = QVBoxLayout()
        self.verticalicerik1Ogretmen.addWidget(QLabel('Öğretmen bilgi1'))
        self.verticalicerik1Ogretmen.addWidget(QLabel('Öğretmen bilgi2'))
        self.verticalicerik1Ogretmen.addWidget(QLabel('Öğretmen bilgi3'))
        self.ogretmenSayfasi.setLayout(self.verticalicerik1Ogretmen)
        self.ogretmenSayfasi.setStyleSheet("color: gray; border-style:solid")
        self.stackedSekmeler.addWidget(self.ogretmenSayfasi)

        self.ayarSayfasi = QWidget()
        self.verticalicerik1Ayar = QVBoxLayout()
        self.verticalicerik1Ayar.addWidget(QLineEdit("Bilgi-1 girin"))
        self.verticalicerik1Ayar.addWidget(QLineEdit("Bilgi-2 girin"))
        self.verticalicerik1Ayar.addWidget(QLineEdit("Bilgi-3 girin"))
        self.ayarSayfasi.setLayout(self.verticalicerik1Ayar)
        self.ayarSayfasi.setStyleSheet("background-color: olive;")
        self.stackedSekmeler.addWidget(self.ayarSayfasi)

        anaYerlesim.addLayout(self.verticalicerik1Butonlar)
        anaYerlesim.addLayout(self.stackedSekmeler)

    def sayfaSec(self,sayfaindexi):
        self.stackedSekmeler.setCurrentIndex(sayfaindexi)

aa = QApplication([])
pencere = AnaPencere()
pencere.show()
aa.exec()


