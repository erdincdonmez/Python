from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()
   
        yatayicerik = QHBoxLayout()
        gridicerik1 = QGridLayout()
        gridicerik2 = QGridLayout()
        gridicerik3 = QGridLayout()
        gridicerik4 = QGridLayout()
        gridicerik1.addWidget(QPushButton('Dene'),2,0)
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)

        gridicerik4.addWidget(QLabel("Label widgeti"),3,1)

        gridicerik1.addWidget(buton1,3,1)
        gridicerik1.addWidget(QPushButton("Buton3"),0,3)
       
        gridicerik2.addWidget(QLabel('Bilgi'),3,2)
        gridicerik2.addWidget(QLabel('Label2'),2,3)
        gridicerik2.addWidget(QLabel('Label3'),1,1)

        gridicerik3.addWidget(QLineEdit())
        gridicerik3.addWidget(QLineEdit())

        yatayicerik.addLayout(gridicerik2)
        yatayicerik.addLayout(gridicerik3)
        yatayicerik.addLayout(gridicerik1)
        yatayicerik.addLayout(gridicerik4)

        araclar = QWidget()
        araclar.setLayout(yatayicerik)
        self.setCentralWidget(araclar)

aa = QApplication([])

pencere = AnaPencere()
pencere.show()

aa.exec()
