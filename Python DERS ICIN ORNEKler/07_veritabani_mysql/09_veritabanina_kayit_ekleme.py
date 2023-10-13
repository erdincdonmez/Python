import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qwe321",
  database="pythondersleri"
)

mycursor = mydb.cursor()

sql = "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
val = ("Erhan AKYOL", "05336235547")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "kayıt eklendi.")