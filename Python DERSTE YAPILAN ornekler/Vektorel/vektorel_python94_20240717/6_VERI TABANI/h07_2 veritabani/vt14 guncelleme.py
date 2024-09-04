import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()
sql = "UPDATE ogrenciler SET telefon = '05364445566' WHERE ad= 'Ensar BUDAK'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt değiştirildi.")