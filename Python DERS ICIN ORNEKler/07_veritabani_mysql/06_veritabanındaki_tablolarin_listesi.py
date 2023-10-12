# veritabanı dosyasındaki tabloların listesi
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qwe321",
  database="pythondersleri"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)