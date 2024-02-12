import sys
# from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
aaa = QPushButton("Tıkla")
aaa.show()
label = QLabel('Merhaba!')
label.show()
app.exec()