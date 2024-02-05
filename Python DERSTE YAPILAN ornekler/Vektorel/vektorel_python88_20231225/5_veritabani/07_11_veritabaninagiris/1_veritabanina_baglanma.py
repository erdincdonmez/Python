# veritabanı sistemine bağlanma
import mysql.connector
xxx = mysql.connector.connect(
  host="localhost", # Server.
  user="root", # Kullanıcı adı.
  password="1234" # Şifre
)
print("Bağlanılan veritabanı:", xxx)

