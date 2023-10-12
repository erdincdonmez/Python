# primary key i var olan bir tablodaki alanlara ekleme.
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="pythondersleri"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")