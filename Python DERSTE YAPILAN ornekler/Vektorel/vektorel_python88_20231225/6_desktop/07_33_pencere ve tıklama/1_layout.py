# Buton ekleyelim
from PyQt6.QtWidgets import *
aa = QApplication([])

ww = QWidget()

icerik = QHBoxLayout()

icerik.addWidget(QPushButton('Tıkla'))
icerik.addWidget(QPushButton('Dene'))
icerik.addWidget(QLabel('Bilgi'))

ww.setLayout(icerik)

ww.show()
aa.exec()



