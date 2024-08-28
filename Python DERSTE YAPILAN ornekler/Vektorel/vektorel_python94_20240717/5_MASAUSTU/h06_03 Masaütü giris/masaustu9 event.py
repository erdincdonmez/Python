from PyQt6.QtWidgets import *
aa = QApplication([])

def tiklama():
    alert = QMessageBox()
    alert.setText('Tıkladın!')
    alert.exec()

pencere = QWidget()

icerik = QVBoxLayout()

icerik.addWidget(QPushButton('Dene'))
buton1 = QPushButton('Tıkla')
icerik.addWidget(buton1)

buton1.clicked.connect(tiklama)

icerik.addWidget(QLabel('Bilgi'))

pencere.setLayout(icerik)

pencere.show()
aa.exec() 