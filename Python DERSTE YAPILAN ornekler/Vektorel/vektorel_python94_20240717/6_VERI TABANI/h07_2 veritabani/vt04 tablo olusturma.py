import mysql.connector

VeriTabani1 = mysql.connector.connect(
  host="localhost", # default olanı localhost.
  user="root", # default olanı root.
  password="1234", # MySQL WorkBench kurarken yazdığınız şifre
  database="pythondersleri"
)

secilenVT = VeriTabani1.cursor()
# secilenVT.execute("CREATE TABLE ogrenciler \
secilenVT.execute("CREATE TABLE ogretmenler \
    (ad VARCHAR(255), telefon VARCHAR(255), brans VARCHAR(255))")