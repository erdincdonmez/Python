import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()
# sql = "DROP TABLE ogrenciler1"
sql = "DROP TABLE IF EXISTS ogrenciler1"
mycursor.execute(sql)