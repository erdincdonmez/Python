# Buton ekleyelim
from PyQt5.QtWidgets import *
aa = QApplication([])
ww = QWidget() # pencere

icerik = QVBoxLayout()

icerik.addWidget(QPushButton('Tıkla'))
icerik.addWidget(QPushButton('Dene'))
icerik.addWidget(QLabel('Bilgi'))

ww.setLayout(icerik)

ww.show()
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
