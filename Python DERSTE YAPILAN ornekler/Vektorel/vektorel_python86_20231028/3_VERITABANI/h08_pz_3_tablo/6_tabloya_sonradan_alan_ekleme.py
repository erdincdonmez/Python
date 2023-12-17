# primary key i var olan bir tablodaki alanlara ekleme.
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN numara1 VARCHAR(10)")
a = input()
