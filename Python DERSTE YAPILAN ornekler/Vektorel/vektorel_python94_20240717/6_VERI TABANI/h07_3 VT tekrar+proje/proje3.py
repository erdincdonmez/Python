import sys
from PyQt6.QtWidgets import *
import rehber
import mysql.connector


# veritabani = baglanti = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "1234",
# )
# mycursor = veritabani.cursor()
# mycursor.execute("CREATE DATABASE rehber")

veritabani = baglanti = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "rehber"
)
secilenVeritabani = veritabani.cursor()
print("Bağlantı tamam..")

secilenVeritabani.execute("CREATE TABLE IF NOT EXISTS kullanicilar (kullaniciAdi VARCHAR(50), sifre VARCHAR(30))")
# komut = "INSERT INTO kullanicilar (kullaniciAdi, sifre) VALUES (%s, %s)"
# parametreDegerleri = ('q', 'qq')
# secilenVeritabani.execute(komut, parametreDegerleri)
# veritabani.commit() # cursor ile olanı değil.

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
        self.close()  # Login penceresini kapat
        self.rehberEkrani = rehber.AnaPencere()
        self.rehberEkrani.show()

    def kontrolEt1(self):
        ka = self.username_input.text()
        sf = self.password_input.text()

        try:
            secilenVeritabani.execute(f"SELECT * FROM kullanicilar where kullaniciAdi='{ka}'")
            bilgiler = secilenVeritabani.fetchone()
            print("Veriatabanından alınan türü: ",type(bilgiler))
            print("bilgiler[0]: ",bilgiler[0])
            print("bilgiler[1]: ",bilgiler[1])
            print("Veriatabanından alınan türü: ",type(bilgiler))
            print("Veriatabanından alınanlar  : ",*bilgiler,sep="   ")


            print(f"Birinci kutuya {ka}, ikinci kutuya {sf} girdiniz.")

            # self.close()
            # self.rehberEkrani = rehber.AnaPencere()
            # self.rehberEkrani.show()

            # Kullanıcı adı ve şifreyi kontrolEt etme - Örnek amaçlı basit bir kontrol
            if ka == bilgiler[0] and sf == bilgiler[1]:
                self.rehberiAc()

            else:
                QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")
        except:
            print("Sorgu hatası")

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





# try:
#     # global veritabani
#     veritabani = baglanti = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "1234",
#         database = "rehber"
#     )
#     print("BAğlantı tamam..")
# except:   
#     print("Veri tabanına bağlanılamadı..\nMuhtelemelen veri tabanı yok.\n\n")
#     try:
#         mycursor = veritabani.cursor()
#         mycursor.execute("CREATE DATABASE rehber")
#         print("Veri tabanı oluşturuldu..")
#     except:
#         print("Veri tabanı oluşturulamadı..")

#     try:
#         veritabani = baglanti = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             password = "1234",
#             database = "rehber"
#         )
#         print("BAğlantı tamam2..")
#     except:
#         print("Bağlantı yine tamam değil..")

