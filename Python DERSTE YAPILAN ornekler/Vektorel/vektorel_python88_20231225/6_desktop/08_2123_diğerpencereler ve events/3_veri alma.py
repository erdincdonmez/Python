import sys
from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        self.yazmakutusu = QLineEdit()
        icerik.addWidget(self.yazmakutusu)
        self.veri = self.yazmakutusu.text()
        buton1 = QPushButton("Çevir")
        icerik.addWidget(buton1)
        buton1.clicked.connect(self.tiklama)
        self.label1 = QLabel("Sonuç: ")
        self.label1.setStyleSheet("border: 1px solid red;color: blue;")
        icerik.addWidget(self.label1)
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def tiklama(self):
        # self.label1.setText("yeni metin")
        self.label1.setText(self.label1.text()+self.yazmakutusu.text()*3)

uygulama = QApplication(sys.argv)
pencere = ceviriPenceresi()
pencere.show()
uygulama.exec() 