# belli kritere uyan kayıtlar LIKE
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="vektorel"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM ogrenciler WHERE adi LIKE '%er%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
