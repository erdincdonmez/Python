# bazı sütünlar
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT ad FROM ogrenciler")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
