import sys
from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rehberim")

        central_widget = QWidget()
        layout = QVBoxLayout()

        label_baslik = QLabel("REHBER 1.0")
        layout.addWidget(label_baslik)


        buton_listele = QPushButton("Listele")
        buton_listele.clicked.connect(self.mesaj)
        layout.addWidget(buton_listele)

        buton_ekle = QPushButton("Ekle")
        buton_ekle.clicked.connect(self.mesaj)
        layout.addWidget(buton_ekle)

        buton_degistir = QPushButton("Degistir")
        buton_degistir.clicked.connect(self.mesaj)
        layout.addWidget(buton_degistir)


        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
  
def main():
    app = QApplication(sys.argv)
    window = AnaPencere()
    QMessageBox.information(window, "Cm-Inch Çevirici", "Inch çevirici uygulamasına hoş geldiniz.")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
