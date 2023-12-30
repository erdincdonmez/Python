from PyQt6.QtWidgets import *
aa = QApplication([])

def tiklama():
    alert = QMessageBox()
    alert.setText('Tıkladın!')
    alert.exec()

pencere = QWidget()
pencere.setWindowTitle("Tıklama örneği")
icerik = QVBoxLayout()

icerik.addWidget(QPushButton('Dene'))
buton1 = QPushButton('Tıkla')
buton1.clicked.connect(tiklama)
icerik.addWidget(buton1)

icerik.addWidget(QLabel('Bilgi'))

pencere.setLayout(icerik)

pencere.show()
aa.exec() 
