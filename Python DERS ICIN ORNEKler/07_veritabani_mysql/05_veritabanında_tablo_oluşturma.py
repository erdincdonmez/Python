import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qwe321",
  database="pythondersleri"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE ogrenciler (ad VARCHAR(255), telefon VARCHAR(255))")
