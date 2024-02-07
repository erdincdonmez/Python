import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="deneme1"
)

mycursor = mydb.cursor()

ad = input("Kaydedilecek isim   :")
no = input("Kaydedilecek numara :")
a= "INSERT INTO ogrenciler (adSoyad, numara) VALUES (%s, %s)"
b= (ad, no)
mycursor.execute(a, b) 

mydb.commit()

print(mycursor.rowcount, "kayıt eklendi.")