import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="OKULVT"
)

mycursor = mydb.cursor()

a= "INSERT INTO ogrenciler (AdSoyad, Telefon) VALUES (%s, %s)"
b= ("Ensar BUDAK", "05446235847")
mycursor.execute(a, b) 

mydb.commit()

print(mycursor.rowcount, "kayıt eklendi.")