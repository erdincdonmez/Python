import mysql.connector
try:
    baglanti = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345"
    )
    print("BAğlantı tamam..")
except:
    print("Veri tabanına bağlanılamadı..")

