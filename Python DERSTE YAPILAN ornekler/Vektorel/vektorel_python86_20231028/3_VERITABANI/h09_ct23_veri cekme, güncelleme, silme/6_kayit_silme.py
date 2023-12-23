import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="vektorel"
)

mycursor = mydb.cursor()
sql = "DELETE FROM ogrenciler WHERE tc LIKE '%7'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt silindi.")