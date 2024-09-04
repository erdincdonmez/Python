import mysql.connector

VeriTabani1 = mysql.connector.connect(
  host="localhost", # default olanı localhost.
  user="root", # default olanı root.
  password="1234", # MySQL WorkBench kurarken yazdığınız şifre
  database="pythondersleri"
)

secilenVT = VeriTabani1.cursor()

a = "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
b = ('Ensar BUDAK', '05446235847')

secilenVT.execute(a, b)

VeriTabani1.commit() # cursor ile olanı değil.