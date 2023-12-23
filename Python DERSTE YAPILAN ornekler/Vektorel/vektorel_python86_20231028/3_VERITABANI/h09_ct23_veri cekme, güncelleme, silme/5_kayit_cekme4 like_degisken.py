# belli kritere uyan kayıtlar LIKE
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="vektorel"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM ogrenciler WHERE adi LIKE %s"
a = input("Aradığınız: ")
aranan = f"%{a}%"
val=(aranan,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
