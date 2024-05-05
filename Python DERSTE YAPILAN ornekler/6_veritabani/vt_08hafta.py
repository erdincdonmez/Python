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
    self.dugme3 = QPushButton('Ara')
    icerik.addWidget(self.dugme3)
    self.dugme4 = QPushButton('Sil')
    icerik.addWidget(self.dugme4)
    self.dugme5 = QPushButton('Düzelt')
    icerik.addWidget(self.dugme5)

    self.dugme1.clicked.connect(self.ekle)
    self.dugme2.clicked.connect(self.listele)
    self.dugme3.clicked.connect(self.ara)
    self.dugme4.clicked.connect(self.sil)
    self.dugme5.clicked.connect(self.duzelt)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def ekle(self):
    self.close()
    self.ekleme = EkleEkrani('Kayıt Ekleme')
    self.ekleme.show()

  def listele(self):
    self.close()
    self.listeleme = VeriListeEkrani('Kayıt Ekleme')
    self.listeleme.show()

  def ara(self):
    self.close()
    self.arama = AramaEkrani('Kayıt Arama')
    self.arama.show()

  def sil(self):
    self.close()
    self.silme = SilmeEkrani('Kayıt Silme')
    self.silme.show()

  def duzelt(self):
    self.close()
    self.duzeltme = DuzeltmeEkrani('Kayıt Düzeltme')
    self.duzeltme.show()



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

class EkleEkrani(QMainWindow):
  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    icerik.addWidget(QLabel('Ad soyad:'))
    self.edit1 = QLineEdit('')
    # self.edit1.width(50)
    icerik.addWidget(self.edit1)
    icerik.addWidget(QLabel('Numara'))
    self.edit2 = QLineEdit()
    icerik.addWidget(self.edit2)
    self.dugme1 = QPushButton('Kaydet')
    icerik.addWidget(self.dugme1)

    self.dugme1.clicked.connect(self.kaydet)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def kaydet(self):
    t1 = self.edit1.text()
    t2 = self.edit2.text()
    print("Edit 1 içeriği:", t1)
    print("Edit 2 içeriği:", t2)
    
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    svt.execute("CREATE TABLE IF NOT EXISTS isimler(id INTEGER PRIMARY KEY AUTOINCREMENT,ad,nu)")
    svt.execute(f"INSERT INTO isimler(ad,nu) VALUES ('{t1}','{t2}')")
    vt.commit()
    vt.close()

    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran() # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

class VeriListeEkrani(QMainWindow):
  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)

    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    liste = svt.execute(f"SELECT * FROM isimler")
    
    # icerik = QVBoxLayout()
    icerik = QGridLayout()
    x = 1
    icerik.addWidget(QLabel('Adı'),0,1)
    icerik.addWidget(QLabel('Numarası'),0,2)
    for a in liste: 
        print (a[1],a[2])
        icerik.addWidget(QLabel(a[1]),x,1) # gridLayout taki x.satır ve 1.sütuna QLable yerleştir.
        icerik.addWidget(QLabel(a[2]),x,2)
        x+=1

    # icerik.setColumnStretch(0, 2) # buna benzer bir şey ile hücre birleştirmesi yapılabilir.
    self.d1 = QPushButton('Ana ekrana dön')
    icerik.addWidget(self.d1,x,1) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
    self.d1.clicked.connect(self.anaEkranaDon)

    araclar = QWidget() # Pencere widgeti oluştur.
    araclar.setLayout(icerik) # Pencere widgeti için layout ata
    self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata
    vt.close()

  def anaEkranaDon(self):
    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran('Ana ekran') # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

class AramaEkrani(QMainWindow):
  def anaEkranaDon(self):
    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran('Ana ekran') # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)
   
    # icerik = QVBoxLayout()
    self.icerik = QGridLayout()
    self.silinecek = QLineEdit()
    self.icerik.addWidget(self.silinecek,0,0)
    getirB = QPushButton('Getir')
    self.icerik.addWidget(getirB,1,0)
    self.bulunanlar = []
    getirB.clicked.connect(self.getir)
    print("bulunanlar:",self.bulunanlar)
    self.icerik.addWidget(QLabel('Id'),0,1)
    self.icerik.addWidget(QLabel('Adı'),0,2)
    self.icerik.addWidget(QLabel('Numarası'),0,3)
    # adL = QLabel('...')
    # nuL = QLabel('...')

 
    # self.icerik.setColumnStretch(0, 2) # buna benzer bir şey ile hücre birleştirmesi yapılabilir.
    self.d1 = QPushButton('Ana ekrana dön')
    self.icerik.addWidget(self.d1,3,0) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
    self.d1.clicked.connect(self.anaEkranaDon)

    araclar = QWidget() # Pencere widgeti oluştur.
    araclar.setLayout(self.icerik) # Pencere widgeti için layout ata
    self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata

  def getir(self):
    silinecekVeri = self.silinecek.text()
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    gelen = svt.execute(f"SELECT * FROM isimler WHERE ad='{silinecekVeri}'")
    x=1
    for a in gelen:
      print(a[0],a[1],a[2])
      self.icerik.addWidget(QLabel(str(a[0])),x,1)
      self.icerik.addWidget(QLabel(str(a[1])),x,2)
      self.icerik.addWidget(QLabel(str(a[2])),x,3)
      x+=1

    vt.close()

class SilmeEkrani(QMainWindow):
  def anaEkranaDon(self):
    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran('Ana ekran') # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)
   
    # icerik = QVBoxLayout()
    self.icerik = QGridLayout()
    self.silinecek = QLineEdit()
    self.icerik.addWidget(self.silinecek,0,0)
    getirB = QPushButton('Getir')
    self.icerik.addWidget(getirB,1,0)
    self.bulunanlar = []
    getirB.clicked.connect(self.getir)
    print("bulunanlar:",self.bulunanlar)
    self.icerik.addWidget(QLabel('Id'),0,1)
    self.icerik.addWidget(QLabel('Adı'),0,2)
    self.icerik.addWidget(QLabel('Numarası'),0,3)
    # adL = QLabel('...')
    # nuL = QLabel('...')

    self.silinecekId = QLineEdit()
    self.icerik.addWidget(self.silinecekId,3,0)
    self.silB = QPushButton('Sil')
    self.icerik.addWidget(self.silB,4,0)
    self.silB.clicked.connect(self.sil)

 
    # self.icerik.setColumnStretch(0, 2) # buna benzer bir şey ile hücre birleştirmesi yapılabilir.
    self.d1 = QPushButton('Ana ekrana dön')
    self.icerik.addWidget(self.d1,5,0) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
    self.d1.clicked.connect(self.anaEkranaDon)

    araclar = QWidget() # Pencere widgeti oluştur.
    araclar.setLayout(self.icerik) # Pencere widgeti için layout ata
    self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata

  def getir(self):
    silinecekVeri = self.silinecek.text()
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    gelen = svt.execute(f"SELECT * FROM isimler WHERE ad='{silinecekVeri}'")
    x=1
    silinecek = []
    for a in gelen:
      print(a[0],a[1],a[2])
      self.icerik.addWidget(QLabel(str(a[0])),x,1)
      self.icerik.addWidget(QLabel(str(a[1])),x,2)
      self.icerik.addWidget(QLabel(str(a[2])),x,3)
      silinecek.append(str(a[0]))
      x+=1
  
    vt.close()

  def sil(self):
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    print("self.silinecekId.text()",self.silinecekId.text())
    svt.execute(f"DELETE FROM isimler WHERE id='{self.silinecekId.text()}'")
    vt.commit()
    vt.close()
    self.close()
    self.liste = VeriListeEkrani()
    self.liste.show()
        
class DuzeltmeEkrani(QMainWindow):
  def anaEkranaDon(self):
    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran('Ana ekran') # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)
   
    # icerik = QVBoxLayout()
    self.icerik = QGridLayout()
    self.silinecek = QLineEdit()
    self.icerik.addWidget(self.silinecek,0,0)
    getirB = QPushButton('Getir')
    self.icerik.addWidget(getirB,1,0)

    getirB.clicked.connect(self.getir)
    # print("bulunanlar:",self.bulunanlar)
    self.icerik.addWidget(QLabel('Id'),0,1)
    self.icerik.addWidget(QLabel('Adı'),0,2)
    self.icerik.addWidget(QLabel('Numarası'),0,3)
    self.duzelecekId = QLineEdit("Düzelcek id")
    self.icerik.addWidget(self.duzelecekId,3,0)

    self.yeniAd = QLineEdit("yeni ad")
    self.icerik.addWidget(self.yeniAd,4,0)
    self.yeniNumara = QLineEdit("yeni numara")
    self.icerik.addWidget(self.yeniNumara,5,0)

    self.silB = QPushButton('Düzelt')
    self.icerik.addWidget(self.silB,6,0)
    self.silB.clicked.connect(self.duzelt)

    self.d1 = QPushButton('Ana ekrana dön')
    self.icerik.addWidget(self.d1,7,0) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
    self.d1.clicked.connect(self.anaEkranaDon)

    araclar = QWidget() # Pencere widgeti oluştur.
    araclar.setLayout(self.icerik) # Pencere widgeti için layout ata
    self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata

  def getir(self):
    silinecekVeri = self.silinecek.text()
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    gelen = svt.execute(f"SELECT * FROM isimler WHERE ad='{silinecekVeri}'")
    x=1
    silinecek = []
    for a in gelen:
      print(a[0],a[1],a[2])
      self.icerik.addWidget(QLabel(str(a[0])),x,1)
      self.icerik.addWidget(QLabel(str(a[1])),x,2)
      self.icerik.addWidget(QLabel(str(a[2])),x,3)
      silinecek.append(str(a[0]))
      x+=1
  
    vt.close()

  def duzelt(self):
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    print("self.duzelecekId.text()",self.duzelecekId.text())
    # svt.execute(f"DELETE FROM isimler WHERE id='{self.duzelecekId.text()}'")
    svt.execute(f"UPDATE isimler SET ad = '{self.yeniAd.text()}', nu = '{self.yeniNumara.text()}' WHERE id = '{self.duzelecekId.text()}'")
    vt.commit()
    vt.close()
    self.close()
    self.liste = VeriListeEkrani()
    self.liste.show()
        
sifreOlustur()
uygulama = QApplication([])
# pencere = loginPenceresi("Giriş1")
pencere = anaEkran("Giriş1")
pencere.show()
# anaPencere = anaEkran("MENU")
# anaPencere.show()
uygulama.exec() 
# self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
