import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="vektorel"
)

mycursor = mydb.cursor()
sql = "UPDATE ogrenciler SET tc = '666' WHERE adi = 'Enes ÖZ'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt değiştirildi.")
