import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qwe321",
  database="pythondersleri"
)

mycursor = mydb.cursor()

sql = "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
val = ("Enes ÖZ", "05412365214")
mycursor.execute(sql, val)

mydb.commit()

print("1 kayıt eklendi, ID:", mycursor.lastrowid)