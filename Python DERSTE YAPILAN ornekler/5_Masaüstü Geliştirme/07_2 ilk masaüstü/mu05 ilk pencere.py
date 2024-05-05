# Buton ekleyelim
from PyQt5.QtWidgets import *
aa = QApplication([])
ww = QWidget() # pencere
ww1 = QWidget() # pencere

def icerikOlustur(xx):
    xx.addWidget(QPushButton('Tıkla'))
    xx.addWidget(QPushButton('Dene'))
    xx.addWidget(QLabel('Bilgi'))

icerik = QVBoxLayout()
icerikOlustur(icerik)
ww.setLayout(icerik)

icerik2 = QHBoxLayout()
icerikOlustur(icerik2)
ww1.setLayout(icerik2)



ww.show()
ww1.show()
aa.exec()


# Tıklama algılama
from PyQt6.QtWidgets import *

app = QApplication([])
button = QPushButton('Click')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Tıkladın!')
    alert.exec()

button.clicked.connect(on_button_clicked)
button.show()
app.exec()
