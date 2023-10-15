# belli kritere uyan kayıtlar LIKE
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM ogrenciler WHERE ad = %s LIMIT 5 "
aranan = ("Ensar BUDAK",)

mycursor.execute(sql,aranan)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
