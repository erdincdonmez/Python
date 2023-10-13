import mysql.connector

try:
    database=mysql.connector.connect(
        host="localhost",
        user="root",
        password="12344"
    )
    print("Bağlnatı tamam")
except mysql.connector.Error as hata:
    print(f"Hata oluştu. Hata:{hata}")
