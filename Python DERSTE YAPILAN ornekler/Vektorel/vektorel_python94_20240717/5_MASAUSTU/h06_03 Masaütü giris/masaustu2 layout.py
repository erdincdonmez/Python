from PyQt6.QtWidgets import *

uygulama = QApplication([])

pencere = QMainWindow()
pencere.setWindowTitle("Çeviri")

icerik = QVBoxLayout()
# icerik = QHBoxLayout()
icerik.addWidget(QLabel("Çevrilecek: "))
icerik.addWidget(QLineEdit("Buraya cm değeri yaz."))
icerik.addWidget(QPushButton("Çevir"))
icerik.addWidget(QLabel("Sonuç: "))

araclar = QWidget()
araclar.setLayout(icerik)
pencere.setCentralWidget(araclar)
pencere.show()

uygulama.exec()

