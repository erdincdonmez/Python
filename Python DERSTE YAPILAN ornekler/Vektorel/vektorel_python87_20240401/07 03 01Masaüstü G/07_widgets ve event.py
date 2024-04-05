from PyQt6.QtWidgets import *

class girisPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş")
        
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevtrilecek Değer:"))
        icerik.addWidget(QLineEdit())
        hesapla = QPushButton("Çevir")
        icerik.addWidget(hesapla)
        hesapla.clicked.connect(self.tiklama)
        icerik.addWidget(QLabel("Sonuç:"))
        
        pencereIcerigi = QWidget()
        pencereIcerigi.setLayout(icerik)
        self.setCentralWidget(pencereIcerigi)

    def hesaplama(self):
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

        

                         