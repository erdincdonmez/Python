# Buton ekleyelim
from PyQt5.QtWidgets import *
aa = QApplication([])
ww = QWidget() # pencere
ww1 = QWidget() # pencere

def icerikOlustur(xx):
    xx.addWidget(QLabel('Kullanıcı adı:'))
    xx.addWidget(QLineEdit('Kullanıcı adınız...'))
    xx.addWidget(QLabel('Şifre:'))
    xx.addWidget(QLineEdit())
    xx.addWidget(QPushButton('Giriş yap'))

icerik = QVBoxLayout()
icerikOlustur(icerik)
ww.setLayout(icerik)
ww.show()

icerik2 = QHBoxLayout()
icerikOlustur(icerik2)
ww1.setLayout(icerik2)
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
