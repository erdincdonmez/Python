# belli kritere uyan kayıtlar DEĞİŞKEN ile
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="deneme1"
)

mycursor = mydb.cursor()
arnn = input("Aradığınız isim?")
sql = "SELECT * FROM ogrenciler WHERE adSoyad = %s"
aranan = (f"{arnn}",)

mycursor.execute(sql, aranan)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

