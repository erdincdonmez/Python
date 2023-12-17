import mysql.connector
xxx = mysql.connector.connect(host="localhost", user="root", password="1234")

secilenvt = xxx.cursor() # verritabanı seçim işlemi
secilenvt.execute("SHOW DATABASES") # veritabanında SQL komutu çalıştırma işlemi
for x in secilenvt: print(x)