import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("... Uygulaması")
window.setFixedWidth(300)
window.setFixedHeight(200)

layout = QVBoxLayout() # layout = QHBoxLayout()

layout.addWidget(QLabel("Kullanıcı adı:"))
layout.addWidget(QLineEdit())
layout.addWidget(QLabel("Şifre:"))
layout.addWidget(QLineEdit())
layout.addWidget(QCheckBox("Beni hatırla"))
layout.addWidget(QPushButton("Giriş yap"))
layout.addWidget(QLabel("..."))

widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)
window.show()
app.exec()
