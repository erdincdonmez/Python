# bir tanesi
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM ogrenciler")
myresult = mycursor.fetchone()

print(myresult)
