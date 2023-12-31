import sys
from PyQt6.QtWidgets import *
import proje4_moduls.inchCevirici
import proje4_moduls.ogrenciTakip

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
        self.uygulama1 = proje4_moduls.inchCevirici.inchCeviriciWindow()
        self.uygulama1.show()
   
    def uygulama2Tiklanma(self):
        # self.close()  # Login penceresini kapat
        self.uygulama2 = proje4_moduls.ogrenciTakip.OgrenciTakipPenceresi()
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
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def login(self):
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
       
def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()