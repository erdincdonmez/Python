import sys
from PyQt6.QtWidgets import *
import mysql.connector
# sys.path.append('../')
import proje4app
from datetime import datetime
import datetime

veritabaniAdi = "proje3database"
tablo1 = "ogrenciler"
tablo2 = "ogretmenler"

def ogrenciListesiAl(istenenVT):
    baglanti = mysql.connector.connect(
        host= proje4app.veritabani.veritabaniHost, # Veritabanı sistemi adı (instance).
        user= proje4app.veritabani.veritabaniUser, # Veritabanı kullanıcı adı
        password= proje4app.veritabani.veritabaniPass, # Veritabanı sistemi(instance) şifresi
        database = istenenVT
        )
    secilenDB = baglanti.cursor()
    secilenDB.execute(f"SELECT * FROM {tablo1}")
    alinanVeri = secilenDB.fetchall()
    baglanti.close()
    print (alinanVeri)
    # print (alinanVeri[0][1])
    # if len(alinanVeri) > 0 and kullanici == alinanVeri[0][1] and sifre == alinanVeri[0][2]:
    #     return True
    # else: return False
    
    return alinanVeri


class OgrenciTakipPenceresi(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")

        ogrenciListesi = ogrenciListesiAl("proje3database")
       
        layout = QVBoxLayout() # üst Layout
        self.yiginLayout = QStackedLayout() # Stacked layout
        self.setLayout(layout)
       
        # combo box oluşturma ve bağlama
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Öğrenciler", "Öğretmenler"])
        self.pageCombo.activated.connect(self.switchPage)
       
        self.sayfa1 = QWidget() # 1.Sayfa : Hakkında
        self.sayfa1Layout = QFormLayout()
        self.id = str( len(ogrenciListesi)+1 )
        self.tc = QLineEdit()
        self.adSoyad = QLineEdit()
        self.sinif = QLineEdit()
        self.sayfa1Layout.addRow("TC : ", self.tc)
        self.sayfa1Layout.addRow("Adi Soyadi : ", self.adSoyad)
        self.sayfa1Layout.addRow("Sinifi : ", self.sinif)
        buton1 = QPushButton("Ekle")
        
        # print ("Giden: ",id,t,a,str(s))
        buton1.clicked.connect(self.ogrenciEkle)
        self.sayfa1Layout.addWidget(buton1)
        self.ogrenciTable = QTableWidget(5,3)
        # print("=> ",ogrenciListesi)

        self.tabloDoldur()
        self.sayfa1Layout.addWidget(self.ogrenciTable)
        labelBilgi = QLabel ("Bilgi")
        # labelBilgi.setText(str(ogrenciListesi[0][0]))
        labelBilgi.setText(f"{str(len(ogrenciListesi))}adet kayıt listelendi.")
        self.sayfa1Layout.addWidget(labelBilgi)
        self.sayfa1.setLayout(self.sayfa1Layout)
        self.yiginLayout.addWidget(self.sayfa1)

       
        self.sayfa2 = QWidget() # 2.Sayfa : İletişim
        self.sayfa2Layout = QFormLayout()
        self.sayfa2Layout.addRow("Adı Soyadı : ", QLineEdit())
        buton3 = QPushButton("Branş ekle")
        self.sayfa2Layout.addRow("Branşı : ", QLineEdit())
        buton4 = QPushButton("Öğretmen ekle")
        self.sayfa2Layout.addWidget(buton4)
        ogretmenTable = QTableWidget(5,3)
        self.sayfa2Layout.addWidget(ogretmenTable)
        self.sayfa2.setLayout(self.sayfa2Layout)
        self.yiginLayout.addWidget(self.sayfa2)
       
        # üst layout a yerleştirme işlemi
        layout.addWidget(self.pageCombo)
        layout.addLayout(self.yiginLayout)

    def switchPage(self):
        self.yiginLayout.setCurrentIndex(self.pageCombo.currentIndex())

    def tabloDoldur(self):
        ogrenciListesiAl(veritabaniAdi)
        ogrenciListesi = ogrenciListesiAl("proje3database")
        self.ogrenciTable.satirSayisi = len(ogrenciListesi)
        satirSayisi = len(ogrenciListesi)  # 6 rows in your example
        sutunSayisi = len(ogrenciListesi[0])  # 3 columns in your example
        # Set colums and rows in QTableWidget
        self.ogrenciTable.setColumnCount(sutunSayisi)
        self.ogrenciTable.setRowCount(satirSayisi)
        # Loops to add values into QTableWidget
        for row in range(satirSayisi):
            for column in range(sutunSayisi):
                header = self.ogrenciTable.horizontalHeader()       
                # header.setSectionResizeMode(column, QHeaderView.ResizeMode.Stretch)
                header.setSectionResizeMode(column, QHeaderView.ResizeMode.ResizeToContents)
                # Check if value datatime, if True convert to string 
                if isinstance(ogrenciListesi[row][column], datetime.datetime):
                    self.ogrenciTable.setItem(row, column, QTableWidgetItem((ogrenciListesi[row][column].strftime('%d/%m/%Y %H:%M:%S'))))
                else:
                    # print(type(ogrenciListesi[row][column]), " => ",ogrenciListesi[row][column])
                    self.ogrenciTable.setItem(row, column, QTableWidgetItem(( str(ogrenciListesi[row][column]) )))



    def ogrenciEkle(self):
        baglanti = mysql.connector.connect(
            host= proje4app.veritabani.veritabaniHost, # Veritabanı sistemi adı (instance).
            user= proje4app.veritabani.veritabaniUser, # Veritabanı kullanıcı adı
            password= proje4app.veritabani.veritabaniPass, # Veritabanı sistemi(instance) şifresi
            database = veritabaniAdi
            )
        
        tc1 = self.tc.text()
        adSoyad1 = self.adSoyad.text()
        sinif1 = self.sinif.text()
        secilenDB = baglanti.cursor()
        print ("gelen =>", veritabaniAdi, self.id, tc1, adSoyad1, sinif1)
        komut = "INSERT INTO ogrenciler (id, tc, adSoyad, sinif) VALUES (%s, %s, %s, %s)"
        data = (self.id, tc1, adSoyad1, sinif1) 
        # secilenDB.execute(komut)  
        secilenDB.execute(komut, data)  
        # secilenDB.executemany(komut, data)  
        baglanti.commit()
        self.tabloDoldur()