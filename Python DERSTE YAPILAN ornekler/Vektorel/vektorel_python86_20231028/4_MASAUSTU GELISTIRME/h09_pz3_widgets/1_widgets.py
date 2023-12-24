import sys
from PyQt6.QtWidgets import *
app = QApplication(sys.argv)
button = QPushButton("Merhaba")
button.setFixedSize(200, 100)
button.show()
app.exec()