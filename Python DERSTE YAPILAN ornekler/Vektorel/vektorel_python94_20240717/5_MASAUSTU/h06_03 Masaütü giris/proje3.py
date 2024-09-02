import sys
from PyQt6.QtWidgets import *
import rehber

class GirisEkrani(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Ekranı")

        ana_bilesenler = QWidget()
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
        login_button.clicked.connect(self.kontrolEt)
        layout.addWidget(login_button)

        ana_bilesenler.setLayout(layout)
        self.setCentralWidget(ana_bilesenler)
    def kontrolEt(self):
        ka = self.username_input.text()
        sf = self.password_input.text()

        print(f"Birinci kutuya {ka}, ikinci kutuya {sf} girdiniz.")

        # self.close()
        # self.rehberEkrani = rehber.AnaPencere()
        # self.rehberEkrani.show()

        # Kullanıcı adı ve şifreyi kontrolEt etme - Örnek amaçlı basit bir kontrol
        if ka == "q" and sf == "q":
            self.rehberiAc()

        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def rehberiAc(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
        self.close()  # Login penceresini kapat
        self.rehberEkrani = rehber.AnaPencere()
        self.rehberEkrani.show()
def main():
    app = QApplication(sys.argv)
    pencere = GirisEkrani()
    pencere.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()