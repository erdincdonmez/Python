from PyQt6.QtWidgets import *

class girisPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş")
        
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevtrilecek Değer:"))
        veri = QLineEdit()
        icerik.addWidget(veri)
        hesapla = QPushButton("Çevir")
        icerik.addWidget(hesapla)
        hesapla.clicked.connect(self.tiklama)
        self.sonuc = QLabel("Sonuç:")
        icerik.addWidget(self.sonuc)
        
        pencereIcerigi = QWidget()
        pencereIcerigi.setLayout(icerik)
        self.setCentralWidget(pencereIcerigi)

    def hesaplama(self):
        self.sonuc.setText("Tıklandı..")
        print("Butona tıklandı.")
    
    def mesajGoster(self):
        mesaj = QMessageBox()
        mesaj.setText("Butona tıklandı")
        mesaj.exec()
    
    def tiklama(self):
        self.hesaplama()
        self.mesajGoster()

app = QApplication([])

pencere = girisPenceresi()
pencere.show()

app.exec()

        

                         