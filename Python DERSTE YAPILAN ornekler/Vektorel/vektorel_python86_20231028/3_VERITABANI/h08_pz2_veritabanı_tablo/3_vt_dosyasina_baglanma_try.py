# kendi veritabanına bağlanma
import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pythondersleri"
    )
    print("Bağlantı ok.")
except mysql.connector.Error as xxx:
    print("Bağlantı hatası. Detay:",xxx)
