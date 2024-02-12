from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()
   
        icerik = QHBoxLayout()

        butonx = QPushButton("Denememe")
        icerik.addWidget(butonx)
        icerik.addWidget(QPushButton('Dene'))
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)
        butonx.clicked.connect(self.tiklama)

        icerik.addWidget(buton1)
        icerik.addWidget(QLabel('Bilgi'))

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

aa = QApplication([])
pencere = AnaPencere()
pencere.show()
aa.exec()

