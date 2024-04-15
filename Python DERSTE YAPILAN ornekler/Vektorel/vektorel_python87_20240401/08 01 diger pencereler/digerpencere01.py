from PyQt6.QtWidgets import *
import deneme

class loginEkrani(QMainWindow):

    def kontrol(self):
        kadi = self.ka.text()
        sifre = self.sf.text()
        # print("Tıklandı", kadi,sifre)
        if kadi == "admin" and sifre == "123":
            # self.mesajGoster("Giriş yapabilir")
            print("Giriş yapabilir")
            deneme.pencere1()
        else:
            # self.mesajGoster("Hatalı giriş yaptınız")
            print("Hatalı giriş yaptınız")
        # self.mesajGoster()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        icerik = QVBoxLayout() # layout oluşturduk Vertical
          #icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı: "))
        self.ka = QLineEdit()
        icerik.addWidget(self.ka)
        icerik.addWidget(QLabel("Şifre: "))
        self.sf = QLineEdit()
        self.sf.setEchoMode(QLineEdit.EchoMode.Password)
        icerik.addWidget(self.sf)
        buton1 = QPushButton("Giriş yap")
        icerik.addWidget(buton1)
        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

        buton1.clicked.connect(self.kontrol)

uygulama = QApplication([])
pencere = loginEkrani()
pencere.show()
uygulama.exec() 
