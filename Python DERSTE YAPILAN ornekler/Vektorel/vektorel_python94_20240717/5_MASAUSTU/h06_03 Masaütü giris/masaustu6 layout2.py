from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
   
        icerik6_dikey = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Kullanıcı adı"))
        dikeyicerik3.addWidget(QLabel("Şifresi"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())
       

        icerik5_yatay = QHBoxLayout()
        icerik5_yatay.addWidget(QPushButton("İptal"))
        icerik5_yatay.addWidget(QPushButton("Giriş yap"))

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)

        icerik6_dikey.addLayout(yatayicerik)
        icerik6_dikey.addWidget(QCheckBox("Beni hatırla"))
        icerik6_dikey.addLayout(icerik5_yatay)

        pencere = QWidget()
        pencere.setLayout(icerik6_dikey)
        self.setCentralWidget(pencere)

aa = QApplication([])
pencere = AnaPencere()
pencere.show()
aa.exec()
