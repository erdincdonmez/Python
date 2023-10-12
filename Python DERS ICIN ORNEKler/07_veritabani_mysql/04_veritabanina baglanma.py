import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="pythondersleri"
    )
    print ("Bağlantı başarılı")
except mysql.connector.Error as hata:
    print (f"İşlem başarısız. Hata: {hata}")

