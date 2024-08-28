from PyQt6.QtWidgets import *

class CeviriPenceresi(QMainWindow):

    def __init__(self,baslik,g=0,y=0):
        super().__init__()
        self.setWindowTitle(baslik)
        if g!=0 and y!=0: self.resize(g,y)

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

pencere = CeviriPenceresi("Pencere1")
pencere2 = CeviriPenceresi("Pencere2",500,400)
pencere.show()
pencere2.show()

uygulama.exec() 