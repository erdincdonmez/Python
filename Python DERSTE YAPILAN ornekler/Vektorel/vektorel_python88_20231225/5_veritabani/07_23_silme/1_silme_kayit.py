import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="deneme1"
)

mycursor = mydb.cursor()
sql = "DELETE FROM ogrenciler WHERE adSoyad = 'Harun'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt silindi.")