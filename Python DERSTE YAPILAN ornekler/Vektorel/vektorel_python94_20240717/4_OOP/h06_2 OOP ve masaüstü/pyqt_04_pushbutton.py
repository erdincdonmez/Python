import sys
from PyQt6.QtWidgets import *
app = QApplication(sys.argv)

x = QWidget()
x.show()  
window1 = QPushButton("Tıkla")
window1.show()  
aa = QLabel("Merhaba")
aa.show()

app.exec()