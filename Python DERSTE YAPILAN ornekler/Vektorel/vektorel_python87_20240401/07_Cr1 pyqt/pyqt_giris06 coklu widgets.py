from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()
          #icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere2 = ceviriPenceresi()
pencere3 = ceviriPenceresi()
pencere.show()
pencere2.show()
pencere3.show()

uygulama.exec() 
