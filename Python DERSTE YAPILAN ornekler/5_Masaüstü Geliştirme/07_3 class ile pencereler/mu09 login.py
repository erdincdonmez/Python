from PyQt6.QtWidgets import *

class loginPenceresi(QMainWindow):
  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    icerik.addWidget(QLabel('Kullanıcı adı:'))
    icerik.addWidget(QLineEdit('Kullanıcı adınız...'))
    icerik.addWidget(QLabel('Şifre:'))
    icerik.addWidget(QLineEdit())
    icerik.addWidget(QPushButton('Giriş yap'))

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

uygulama = QApplication([])
pencere = loginPenceresi("Giriş")
pencere.show()
uygulama.exec() 
