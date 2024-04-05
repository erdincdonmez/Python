from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class girisPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş")
        
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek Değer:"))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç:"))
        # icerik.addWidget(QPixmap('login1.png'))
        xx = QPixmap('login1.png')
        lab = QLabel()
        lab.setPixmap(xx)
        icerik.addWidget(lab)

        
        pencereIcerigi = QWidget()
        pencereIcerigi.setLayout(icerik)
        self.setCentralWidget(pencereIcerigi)

app = QApplication([])

pencere = girisPenceresi()
pencere.show()

app.exec()

        

                         