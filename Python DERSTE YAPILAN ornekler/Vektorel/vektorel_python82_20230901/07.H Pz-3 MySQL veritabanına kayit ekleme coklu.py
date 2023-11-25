import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM ogrenciler"

mycursor.execute(sql)

ks=0
for a in mycursor:
    ks +=1
    print(a)

print("Kayıt sayısı:",ks)