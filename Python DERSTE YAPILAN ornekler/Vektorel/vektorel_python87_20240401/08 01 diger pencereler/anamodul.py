from PyQt6.QtWidgets import * 
import sys, sqlite3

class AnaEkran(QMainWindow):

    def veriTabaniOlustur(self):
        # vt = sqlite3.connect('rehber.sqlite')
        vt = sqlite3.connect('rehber.db')
        im = vt.cursor()

        im.execute("""CREATE TABLE 'personel dosyasi'
        (ismi', soyismi', memleket)""")

    def __init__(self):
        super().__init__()

        self.veriTabaniOlustur()

        self.setWindowTitle("Rehber uygulaması") # Pencere başlığı

        anaSutun = QVBoxLayout() # Tüm layoutları kapsaması için tanımladık.

        satir1 = QHBoxLayout() # Bu satırlar ana sütun içine yerleşecek.
        satir2 = QHBoxLayout() # Bu satırlar ana sütun içine yerleşecek.
        satir3 = QHBoxLayout() # Bu satırlar ana sütun içine yerleşecek.
        sutun1 = QVBoxLayout() # bu sütunlar satır 2nin içine yerleşecek.
        sutun2 = QVBoxLayout() # bu sütunlar satır 2nin içine yerleşecek.

        # satir1 in içeriği
        baslik = QLabel("Rehber uygulaması")
        satir1.addWidget(baslik)

        # satir2 içindeki sütün1 içeriği
        bilgi1 = QLabel("Ad soyad")
        sutun1.addWidget(bilgi1)
        bilgi2 = QLabel("Telefonu")
        sutun1.addWidget(bilgi2)

        # satir2 içindeki sütün2 içeriği
        self.ad = QLineEdit()
        sutun2.addWidget(self.ad)
        self.tel = QLineEdit()
        sutun2.addWidget(self.tel)

        # satir3 in içeriği
        buton1 = QPushButton("Kaydet")
        satir3.addWidget(buton1)
        buton2 = QPushButton("Listele")
        satir3.addWidget(buton2)

        # satir2 içine sütunları yerleştiriyoruz.
        satir2.addLayout(sutun1)
        satir2.addLayout(sutun2)

        # anaSutun içine diğer satırları yerleştiriyoruz.
        anaSutun.addLayout(satir1)
        anaSutun.addLayout(satir2)
        anaSutun.addLayout(satir3)

        # Pencere ana widgeti (hepsini kapsayacak olan)
        pencereIci = QWidget()
        pencereIci.setLayout(anaSutun) # ana widget içine ana layoutu yerleştiriyoruz.
        self.setCentralWidget(pencereIci) # ana layoutu pencere içine yerleştiriyoruz.

def main():
    app = QApplication([])
    window = AnaEkran()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


# def mesaj(self):
#     cmdeger = int(self.cmdeger_input.text()) * 2
#     self.inch_input.setText(str(cmdeger))

# QMessageBox.information(window, "Cm-Inch Çevirici", "Inch çevirici uygulamasına hoş geldiniz.")