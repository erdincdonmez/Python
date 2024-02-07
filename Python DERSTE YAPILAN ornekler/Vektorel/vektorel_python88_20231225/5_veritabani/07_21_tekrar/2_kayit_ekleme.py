import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="deneme1"
)

mycursor = mydb.cursor()

a= "INSERT INTO ogrenciler (adSoyad, numara) VALUES (%s, %s)"
b= ("Erhan DÖNMEZ", "6549873254")
mycursor.execute(a, b) 

mydb.commit()

print(mycursor.rowcount, "kayıt eklendi.")