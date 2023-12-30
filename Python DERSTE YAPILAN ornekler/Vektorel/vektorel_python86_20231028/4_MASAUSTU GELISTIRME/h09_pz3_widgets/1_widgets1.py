import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
window = QMainWindow()

layout = QVBoxLayout()
# layout = QHBoxLayout()
layout.addWidget(QCheckBox("seç"))
layout.addWidget(QComboBox())
layout.addWidget(QDateEdit())
layout.addWidget(QDateTimeEdit())
layout.addWidget(QDial())
layout.addWidget(QDoubleSpinBox())
layout.addWidget(QFontComboBox())
layout.addWidget(QLCDNumber())
layout.addWidget(QLabel("Label"))
layout.addWidget(QLineEdit())
layout.addWidget(QProgressBar())
layout.addWidget(QPushButton("Tıkla"))
layout.addWidget(QRadioButton("seç"))
layout.addWidget(QSlider())
layout.addWidget(QSpinBox())
layout.addWidget(QTimeEdit())

widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)

window.show()
app.exec()
