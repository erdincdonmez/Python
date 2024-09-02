import mysql.connector

try:
  veritabani = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="1234" # Veritabanı sistemi(instance) şifresi
  )
  print("Bağlantı tamam:")
  print(veritabani)
except:
  print("Veritabanına bağlanırken bir hata oluştu.")
