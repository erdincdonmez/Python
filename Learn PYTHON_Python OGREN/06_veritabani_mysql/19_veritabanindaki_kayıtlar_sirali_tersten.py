# Veritabanındaki kayıtlar SIRA ile TERSTEN
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM ogrenciler ORDER BY ad DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)