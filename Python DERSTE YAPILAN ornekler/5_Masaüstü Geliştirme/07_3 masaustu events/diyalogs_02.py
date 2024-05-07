# Düğmeye basınca gelen BASİT diyalog
import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        yerlesim = QVBoxLayout()      
        buton1 = QPushButton("Diyalog göster!")
        yerlesim.addWidget(QLabel("Basit diyalog gösterme"))
        yerlesim.addWidget(buton1)
        buton1.clicked.connect(self.tiklama2)
        araclar = QWidget()
        araclar.setLayout(yerlesim)
        self.setCentralWidget(araclar)

    def tiklama(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Bilgilendirme!")
        dlg.setText("Buradaki bilgiyi öğrendin.")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:#Düğme sonucu
            print("TAMAM!")

    def tiklama2(self, s):
        button = QMessageBox.question(self, "Başlık", "Mesaj")
        if button == QMessageBox.StandardButton.Yes: print("Yes!")
        else: print("No!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
