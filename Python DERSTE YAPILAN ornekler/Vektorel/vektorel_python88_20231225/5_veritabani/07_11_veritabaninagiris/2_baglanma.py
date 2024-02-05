# veritabanı sistemine bağlanma
import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="1234")
    print("Bağlandı")
    print(mydb)
except mysql.connector.Error as xx:
    print("hata oluştu")
    print(f"hata kodu:\n{xx}")