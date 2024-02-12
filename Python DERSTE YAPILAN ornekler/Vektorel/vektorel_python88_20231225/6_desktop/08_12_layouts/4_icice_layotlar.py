from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Adı"))
        dikeyicerik3.addWidget(QLabel("Soyadı"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())
        
        yatayicerik = QHBoxLayout()
        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)

        pencere = QWidget()
        pencere.setLayout(yatayicerik)
        self.setCentralWidget(pencere)

aa = QApplication([])

pencere = AnaPencere()
pencere.show()

aa.exec()
