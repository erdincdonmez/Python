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
buton1.clicked.connect(tiklama)

icerik.addWidget(buton1)
icerik.addWidget(QLabel('Bilgi'))

pencere.setLayout(icerik)

pencere.show()
aa.exec()





# from PyQt6.QtWidgets import *

# app = QApplication([])
# button = QPushButton('Click')

# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('Tıkladın!')
#     alert.exec()

# button.clicked.connect(on_button_clicked)
# button.show()
# app.exec()
