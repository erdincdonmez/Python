import sys
from PyQt5.QtWidgets import *
# app = QApplication([])
app = QApplication(sys.argv)
pencere = QWidget()
pencere2 = QWidget()
pencere3 = QWidget()
pencere4 = QPushButton("Tıkla ma")
pencere5 = QLabel("Bu bir label widgeti")

pencere.show()
pencere2.show()
pencere3.show()
pencere4.show()
pencere5.show()
app.exec()

# xx = QApplication([])
# pencere = QWidget()
# pencere.show()
# xx.exec()