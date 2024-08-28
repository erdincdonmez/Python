from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
   
        dikeyicerik = QVBoxLayout()

        yatayicerik3 = QHBoxLayout()
        yatayicerik3.addWidget(QLabel("Adı"))
        yatayicerik3.addWidget(QLineEdit())

        yatayicerik4 = QHBoxLayout()
        yatayicerik4.addWidget(QLabel("Soyadı"))
        yatayicerik4.addWidget(QLineEdit())
       
        dikeyicerik.addLayout(yatayicerik3)
        dikeyicerik.addLayout(yatayicerik4)

        pencere = QWidget()
        pencere.setLayout(dikeyicerik)
        self.setCentralWidget(pencere)

aa = QApplication([])
pencere = AnaPencere()
pencere.show()
aa.exec()
