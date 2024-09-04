import mysql.connector

VeriTabani1 = mysql.connector.connect(
  host="localhost", # default olanı localhost.
  user="root", # default olanı root.
  password="1234", # MySQL WorkBench kurarken yazdığınız şifre
  database="pythondersleri"
)

secilenVT = VeriTabani1.cursor()
secilenVT.execute("SELECT * FROM ogrenciler")
liste = secilenVT.fetchall()

print(*liste,sep="\n")
print(len(liste), " adet kayıt var.")