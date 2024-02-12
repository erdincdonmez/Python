# deneyebilirsiniz.
# pencere.resize(300,50)
# pencere.setFixedSize(100, 100)
from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Çeviri")
        # self.setFixedSize(500, 100)

        icerik = QVBoxLayout()
          #icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç: "))
        
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
        
    def baslik(self,x="yok"):
        self.setWindowTitle(x)


uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()
pencere1 = ceviriPenceresi()
pencere1.baslik("Deneme")
pencere1.show()
pencere2 = ceviriPenceresi()
pencere2.show()

uygulama.exec() 