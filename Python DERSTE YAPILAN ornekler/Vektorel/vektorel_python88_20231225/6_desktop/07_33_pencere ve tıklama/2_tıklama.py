# Tıklama algılama
from PyQt6.QtWidgets import *

app = QApplication([])
button = QPushButton('Click')

def aaa():
    alert = QMessageBox()
    alert.setText('Tıkladın!')
    alert.exec()
    print("tıklama gerçekleşti")

button.clicked.connect(aaa)

button.show()
app.exec()

