import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="deneme1"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM ogrenciler")
xxx = mycursor.fetchall()

print(xxx)

