## BAK
import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

window = QMainWindow()
window1 = QMainWindow()

xxx = QHBoxLayout()
# layout = QHBoxLayout()

xxx.addWidget(QLabel("Label"))
xxx.addWidget(QLineEdit())
xxx.addWidget(QLabel("Label"))
xxx.addWidget(QLineEdit())
xxx.addWidget(QPushButton("Tıkla"))

ww = QWidget()
ww.setLayout(xxx)

window.setCentralWidget(ww)

window.show()

tt =QWidget()
tt.setLayout(xxx)
window1.setCentralWidget(tt)
window1.show()

app.exec()
