import mysql.connector
xxx = mysql.connector.connect(
  host="localhost", # Server.
  user="root", # Kullanıcı adı.
  password="1234" # Şifre
)
print("Bağlanılan veritabanı:", xxx)


secilenvt = xxx.cursor() # verritabanı seçim işlemi
secilenvt.execute("SHOW DATABASES") # veritabanında SQL komutu çalıştırma işlemi
for x in secilenvt: print(x)