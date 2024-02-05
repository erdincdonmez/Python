# veritabanı sistemine bağlanma
import mysql.connector
try:
    xxx = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="1234")
    print("Bağlandı")
    print(xxx)

    secilenvt = xxx.cursor() # verritabanı seçim işlemi USE .....
    secilenvt.execute("CREATE DATABASE pytondersleri") # veritabanında SQL komutu çalıştırma işlemi
    print("VT oluştu")

except mysql.connector.Error as xx:
    print("hata oluştu")
    print(f"hata kodu:\n{xx}")
