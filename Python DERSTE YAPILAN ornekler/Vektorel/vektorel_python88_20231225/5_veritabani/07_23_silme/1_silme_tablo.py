import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="deneme2"
)

mycursor = mydb.cursor()
sql = "DROP TABLE ogrenciler"
mycursor.execute(sql)
