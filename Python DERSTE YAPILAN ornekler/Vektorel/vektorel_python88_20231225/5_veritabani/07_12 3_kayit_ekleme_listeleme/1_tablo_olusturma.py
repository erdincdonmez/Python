# veritabanında tablo oluşturma
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="deneme2"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE ogrenciler (AdSoyad VARCHAR(255), Telefon VARCHAR(255))")

