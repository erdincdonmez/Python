# belli kritere uyan kayıtlar DEĞİŞKEN ile
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM ogrenciler WHERE ad LIKE %s ORDER BY ad DESC"
aranan = ("%er%",)

mycursor.execute(sql, aranan)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
