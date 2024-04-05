from PyQt6.QtWidgets import *

class girisPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çevirici")
        
        # icerik = QHBoxLayout() # Yatay içerik için
        icerik = QVBoxLayout() # Dikey içerik için
        
        icerik.addWidget(QLabel("Kullanıcı adı:"))
        self.ka = QLineEdit()
        icerik.addWidget(self.ka)
        

        icerik.addWidget(QLabel("Şifre:"))
        self.sf = QLineEdit()
        icerik.addWidget(self.sf)
        girisButton = QPushButton("Giriş yap")
        icerik.addWidget(girisButton)

        girisButton.clicked.connect(self.kontrolEt)

        self.sonuc = QLabel("Inch karşılığı:")
        icerik.addWidget(self.sonuc)
        
        pencereIcerigi = QWidget()
        pencereIcerigi.setLayout(icerik)
        self.setCentralWidget(pencereIcerigi)

    def hesaplama(self):
        # self.sonuc.setText(self.sonuc.text()+ str(int(self.veri.text())*2) )
        self.sonuc.setText("Inch karşılığı: "+ str(int(self.veri.text())*2) )
        # print("Butona tıklandı."+ int(str(self.veri.text()))*2)
    
    def mesajGoster(self,mesaj):
        mesaj = QMessageBox()
        mesaj.setText(mesaj)
        mesaj.exec()
    
    def kontrolEt(self):
        if self.ka.text() == "admin" and self.sf.text() == "123":
            # self.mesajGoster("Girebilir")
            print("Giriş yapabilir")
        else:
            # self.mesajGoster("Hatalı giriş yaptınız")
            print("Hatalı giriş yaptınız")
        # self.mesajGoster()

app = QApplication([])

pencere = girisPenceresi()
pencere.show()

app.exec()

        

                         