# veritabanı dosyasındaki tabloların listesi
import mysql.connector

xxx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

yyy = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="eticaret"
)

aaa = xxx.cursor()
bbb = yyy.cursor()

aaa.execute("SHOW TABLES")
bbb.execute("SHOW TABLES")

print("pythondersleri veritabanı tabloları")
for x in aaa:
  print(x)

print("eticaret veritabanı tabloları")
for x in bbb:
  print(x)