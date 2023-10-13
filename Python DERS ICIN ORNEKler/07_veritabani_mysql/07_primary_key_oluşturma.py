# primary key kullanarak tablo oluşturma
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE ogrenciler1 (id INT AUTO_INCREMENT PRIMARY KEY, ad VARCHAR(255), telefon VARCHAR(255))")