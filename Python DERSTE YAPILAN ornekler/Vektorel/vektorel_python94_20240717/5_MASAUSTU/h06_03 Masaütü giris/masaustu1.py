import sys
from PyQt6.QtWidgets import *
app = QApplication(sys.argv)

x = QWidget()

x.setWindowTitle('Deneme')
x.resize(300,100)
# x.setFixedSize(100, 100)
x.show() 


window1 = QPushButton("Tıkla")
window1.setWindowTitle('Deneme22')
window1.resize(300,200)
# window1.setFixedSize(100, 100)
window1.show()  
aa = QLabel("Merhaba")
aa.show()

app.exec()
