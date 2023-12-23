import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="vektorel"
)

mycursor = mydb.cursor()

sql = "INSERT INTO ogrenciler (adi, tc) VALUES (%s, %s)"
val = ("Enes ÖZ", "88888888888")
mycursor.execute(sql, val)

mydb.commit()

print("1 kayıt eklendi, ID:", mycursor.lastrowid)