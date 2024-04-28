from PyQt6.QtWidgets import *

def sifreOlustur():
  kullaniciAdi = "adm"
  sifre = "123"
  dosya = open("rhbpwd.txt","w")
  dosya.write(f"{kullaniciAdi} {sifre}")
  dosya.close()



class anaEkran(QMainWindow):
  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    self.dugme1 = QPushButton('Ekle')
    icerik.addWidget(self.dugme1)
    self.dugme2 = QPushButton('Listele')
    icerik.addWidget(self.dugme2)
    self.dugme3 = QPushButton('Sil')
    icerik.addWidget(self.dugme3)

    self.dugme1.clicked.connect(self.ekle)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def ekle(self):
    print("Ekleme tıklandı")


class loginPenceresi(QMainWindow):
  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    icerik.addWidget(QLabel('Kullanıcı adı:'))
    self.edit1 = QLineEdit('Kullanıcı adınız...')
    # self.edit1.width(50)
    icerik.addWidget(self.edit1)
    icerik.addWidget(QLabel('Şifre:'))
    self.edit2 = QLineEdit()
    self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
    icerik.addWidget(self.edit2)
    self.dugme1 = QPushButton('Giriş yap')
    icerik.addWidget(self.dugme1)

    self.dugme1.clicked.connect(self.kontrolEt)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def kontrolEt(self):
    print("Düğmeye tıklandı..")
    t1 = self.edit1.text()
    t2 = self.edit2.text()
    print("Edit 1 içeriği:", t1)
    print("Edit 2 içeriği:", t2)
    dosya = open("rhbgirilenpwd.txt","w")
    dosya.write(f"{t1} {t2}")
    dosya.close()

    if t1=="q" and t2 == "q" :
      print("Giriş ok")
      self.close()
      self.ap = anaEkran()
      self.ap.show()
    else:
      print("İzin yok")
      dlg = QMessageBox(self)
      dlg.setWindowTitle("Bilgilendirme!")
      dlg.setText("İzin yok")
      dlg.exec()

sifreOlustur()
uygulama = QApplication([])
pencere = loginPenceresi("Giriş1")
pencere.show()
# anaPencere = anaEkran("MENU")
# anaPencere.show()
uygulama.exec() 
# self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
