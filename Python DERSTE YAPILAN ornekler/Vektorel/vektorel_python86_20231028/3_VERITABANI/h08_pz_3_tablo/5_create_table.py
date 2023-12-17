# veritabanı dosyasındaki tabloların listesi
import mysql.connector

xxxx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="eticaret"
)

aaa = xxxx.cursor()

aaa.execute("CREATE TABLE stoklar (id INT, ad VARCHAR(255), miktarı INT)")

for x in aaa:
  print(x)