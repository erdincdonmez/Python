from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()
   
        icerik = QHBoxLayout()

        icerik.addWidget(QPushButton('Dene'))
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)

        icerik.addWidget(buton1)
        icerik.addWidget(QLabel('Bilgi'))

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

def calis():
    aa = QApplication([])
    pencere = AnaPencere()
    pencere.show()
    aa.exec()

