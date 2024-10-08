from PyQt6.QtWidgets import *

class girisPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çevirici")
        
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek Değer (cm):"))
        self.veri = QLineEdit()

        icerik.addWidget(self.veri)
        hesapla = QPushButton("Çevir")
        icerik.addWidget(hesapla)
        hesapla.clicked.connect(self.tiklama)
        self.sonuc = QLabel("Inch karşılığı:")
        icerik.addWidget(self.sonuc)
        
        pencereIcerigi = QWidget()
        pencereIcerigi.setLayout(icerik)
        self.setCentralWidget(pencereIcerigi)

    def hesaplama(self):
        # self.sonuc.setText(self.sonuc.text()+ str(int(self.veri.text())*2) )
        self.sonuc.setText("Inch karşılığı: "+ str(int(self.veri.text())*2) )
        # print("Butona tıklandı."+ int(str(self.veri.text()))*2)
    
    def mesajGoster(self):
        mesaj = QMessageBox()
        mesaj.setText("Butona tıklandı")
        mesaj.exec()
    
    def tiklama(self):
        self.hesaplama()
        # self.mesajGoster()

app = QApplication([])

pencere = girisPenceresi()
pencere.show()

app.exec()

        

                         