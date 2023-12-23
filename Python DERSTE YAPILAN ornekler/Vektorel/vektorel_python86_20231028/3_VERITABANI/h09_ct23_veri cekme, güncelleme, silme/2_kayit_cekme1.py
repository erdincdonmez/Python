import mysql.connector

veritabanibilgisi = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="vektorel"
)

secilenvt = veritabanibilgisi.cursor()

sqlkomutu = "SELECT adi,tc FROM ogrenciler"

secilenvt.execute(sqlkomutu)
alinanlar = secilenvt.fetchall()

# print(alinanlar)
for x in alinanlar:
    print(x)

# for x in alinanlar:
#    print(x[0],"\t",x[1])

