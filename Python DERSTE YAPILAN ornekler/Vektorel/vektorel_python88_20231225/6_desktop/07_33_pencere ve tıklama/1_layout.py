# Buton ekleyelim
from PyQt6.QtWidgets import *
aa = QApplication([])

pencere = QWidget()

icerik = QVBoxLayout()

icerik.addWidget(QPushButton('Tıkla'))
icerik.addWidget(QPushButton('Dene'))
icerik.addWidget(QLabel('Bilgi'))

pencere.setLayout(icerik)

pencere.show()
aa.exec()



