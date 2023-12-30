from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()
   
        yatayicerik = QHBoxLayout()
        dikeyicerik1 = QVBoxLayout()
        dikeyicerik2 = QVBoxLayout()
        dikeyicerik3 = QVBoxLayout()
        dikeyicerik4 = QVBoxLayout()

        dikeyicerik1.addWidget(QPushButton('Dene'))
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)

        dikeyicerik4.addWidget(QLabel("Label widgeti"))

        dikeyicerik1.addWidget(buton1)
        dikeyicerik1.addWidget(QPushButton("Buton3"))
       
        dikeyicerik2.addWidget(QLabel('Bilgi'))
        dikeyicerik2.addWidget(QLabel('Label2'))
        dikeyicerik2.addWidget(QLabel('Label3'))

        dikeyicerik3.addWidget(QLineEdit())
        dikeyicerik3.addWidget(QLineEdit())

        yatayicerik.addLayout(dikeyicerik2)
        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik1)
        yatayicerik.addLayout(dikeyicerik4)

        araclar = QWidget()
        araclar.setLayout(yatayicerik)
        self.setCentralWidget(araclar)

class yavrupencere(QMainWindow):
    def __init__(self):
        super().__init__()
        dikeyicerik1 = QVBoxLayout()
        dikeyicerik1.addWidget(QPushButton('Dene2'))
        dikeyicerik1.addWidget(QPushButton('Dene3'))
        araclar = QWidget()
        araclar.setLayout(dikeyicerik1)
        self.setCentralWidget(araclar)


aa = QApplication([])

pencere = AnaPencere()
pencere.show()



aa.exec()
