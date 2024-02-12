import sys
from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Evrensel Uygulama")
        self.arayuz()

    def arayuz(self):
        ana_widget = QWidget()
        layout = QVBoxLayout()
       
        layout.addWidget(QLabel("Hangi uygulamayı kullanacaksın?"))

        uygulama1 = QPushButton("Inch Çevirici")
        uygulama1.clicked.connect(self.uygulama1Tiklanma)
        layout.addWidget(uygulama1)

        uygulama2 = QPushButton("uygulama2")
        uygulama2.clicked.connect(self.uygulama2Tiklanma)
        layout.addWidget(uygulama2)

        ana_widget.setLayout(layout)
        self.setCentralWidget(ana_widget)

    def uygulama1Tiklanma(self):
        # self.close()  # Login penceresini kapat
        self.uygulama1 = InchCevirici()
        self.uygulama1.show()
   
    def uygulama2Tiklanma(self):
        # self.close()  # Login penceresini kapat
        self.uygulama2 = OgrenciUygulamasi()
        self.uygulama2.show()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Ekranı")
        self.arayuz()

    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        label_username = QLabel("Kullanıcı Adı:")
        self.username_input = QLineEdit()
        layout.addWidget(label_username)
        layout.addWidget(self.username_input)

        label_password = QLabel("Şifre:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(label_password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Giriş Yap")
        login_button.clicked.connect(self.loginOlayi)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def loginOlayi(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Kullanıcı adı ve şifreyi kontrol etme - Örnek amaçlı basit bir kontrol
        if username == "q" and password == "q":
            self.open_AnaEkran()
        else: QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def open_AnaEkran(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
        self.close()  # Login penceresini kapat
        self.anaEkran = AnaPencere()
        self.anaEkran.show()

class InchCevirici(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inch çevirici")
        self.arayuz()

    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        label_cmdeger = QLabel("Cm değeri girin:")
        self.cmdeger_input = QLineEdit()
        layout.addWidget(label_cmdeger)
        layout.addWidget(self.cmdeger_input)

        cevir_button = QPushButton("Çevir")
        cevir_button.clicked.connect(self.mesaj)
        layout.addWidget(cevir_button)

        label_inch = QLabel("Inch değeri:")
        self.inch_input = QLineEdit()
        layout.addWidget(label_inch)
        layout.addWidget(self.inch_input)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
       
class OgrenciUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
       
        layout = QVBoxLayout() # üst Layout
        self.yiginLayout = QStackedLayout() # Stacked layout
        self.setLayout(layout)
       
        # combo box oluşturma ve bağlama
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Hakkında", "İletişim"])
        self.pageCombo.activated.connect(self.switchPage)
       
        self.sayfa1 = QWidget() # 1.Sayfa : Hakkında
        self.sayfa1Layout = QFormLayout()
        self.sayfa1Layout.addRow("İsim : ", QLineEdit())
        self.sayfa1Layout.addRow("İşi : ", QLineEdit())
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

def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

