import sys
from PyQt5.QtWidgets import *
# app = QApplication([])
app = QApplication(sys.argv)
pencere = QWidget()
pencere.setWindowTitle('Deneme')
pencere.resize(300,50)
# pencere.setFixedSize(100, 100)

pencere.show()

app.exec()

# xx = QApplication([])
# pencere = QWidget()
# pencere.show()
# xx.exec()