import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="okulvt"
)

mycursor = mydb.cursor()

# listeleme
mycursor.execute("SELECT * FROM ogrenciler")
xxx = mycursor.fetchall()

for x in xxx:
    for a in x:
        print(a,end=" ")
    print()

# güncelleme
# sql = "UPDATE ogrenciler SET adiSoyadi = 'Ensar BUDAK1' WHERE adiSoyadi = 'Ensar BUDAK'"
sql = "UPDATE ogrenciler SET numarasi = '4445444' WHERE adiSoyadi = 'Ensar BUDAK1'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt değiştirildi.")
# bitiş güncelleme 

print("-------- GÜNCELLENMİŞ HALİ ----------")
mycursor.execute("SELECT * FROM ogrenciler")
xxx = mycursor.fetchall()

for x in xxx:
    for a in x:
        print(a,end=" ")
    print()