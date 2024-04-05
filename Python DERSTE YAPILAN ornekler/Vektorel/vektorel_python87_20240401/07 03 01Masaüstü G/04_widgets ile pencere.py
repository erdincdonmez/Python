from PyQt6.QtWidgets import *

class girisPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş")
        
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevtrilecek Değer:"))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç:"))
        
        pencereIcerigi = QWidget()
        pencereIcerigi.setLayout(icerik)
        self.setCentralWidget(pencereIcerigi)

app = QApplication([])

pencere = girisPenceresi()
pencere.show()

app.exec()

        

                         