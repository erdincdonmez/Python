import sys

from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        layout.addWidget(QCheckBox())
        layout.addWidget(QComboBox())
        layout.addWidget(QDateEdit())
        layout.addWidget(QDateTimeEdit())
        layout.addWidget(QDial())
        layout.addWidget(QDoubleSpinBox())
        layout.addWidget(QFontComboBox())
        layout.addWidget(QLCDNumber(5))
        layout.addWidget(QLabel("----"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QProgressBar())
        layout.addWidget(QPushButton())
        layout.addWidget(QRadioButton())
        layout.addWidget(QSlider())
        layout.addWidget(QSpinBox())
        layout.addWidget(QTimeEdit())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

