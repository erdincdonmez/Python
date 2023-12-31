import sys
from PyQt6.QtWidgets import *

class OgrenciTakipPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
       
        layout = QVBoxLayout() # üst Layout
        self.yiginLayout = QStackedLayout() # Stacked layout
        self.setLayout(layout)
       
        # combo box oluşturma ve bağlama
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Öğrenciler", "Öğretmenler"])
        self.pageCombo.activated.connect(self.switchPage)
       
        self.sayfa1 = QWidget() # 1.Sayfa : Hakkında
        self.sayfa1Layout = QFormLayout()
        self.sayfa1Layout.addRow("Adi Soyadi : ", QLineEdit())
        self.sayfa1Layout.addRow("Sinifi : ", QLineEdit())
        # buton1 = QPushButton("Ekle")
        # self.sayfa1Layout.addWidget(buton1)
        self.sayfa1.setLayout(self.sayfa1Layout)
        self.yiginLayout.addWidget(self.sayfa1)

       
        self.sayfa2 = QWidget() # 2.Sayfa : İletişim
        self.sayfa2Layout = QFormLayout()
        self.sayfa2Layout.addRow("Adresi : ", QLineEdit())
        self.sayfa2Layout.addRow("Telefonu : ", QLineEdit())
        self.sayfa2.setLayout(self.sayfa2Layout)
        self.yiginLayout.addWidget(self.sayfa2)
       
        # üst layout a yerleştirme işlemi
        layout.addWidget(self.pageCombo)
        layout.addLayout(self.yiginLayout)

    def switchPage(self):
        self.yiginLayout.setCurrentIndex(self.pageCombo.currentIndex())
