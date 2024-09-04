import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()
sql = "DELETE FROM ogrenciler WHERE ad='Alper TOY'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt silindi.")