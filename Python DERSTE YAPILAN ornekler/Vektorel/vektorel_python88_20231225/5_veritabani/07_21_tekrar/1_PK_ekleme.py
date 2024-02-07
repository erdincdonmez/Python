# primary key i var olan bir tablodaki alanlara ekleme.
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="deneme1"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")