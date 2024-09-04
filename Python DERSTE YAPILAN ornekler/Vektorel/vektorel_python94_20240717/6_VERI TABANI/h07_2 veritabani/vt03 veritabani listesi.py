import mysql.connector

VeriTabani1 = mysql.connector.connect(
  host="localhost", # default olanı localhost.
  user="root", # default olanı root.
  password="1234" # MySQL WorkBench kurarken yazdığınız şifre
)

secilenVT = VeriTabani1.cursor()
secilenVT.execute("SHOW DATABASES")
liste = secilenVT.fetchall()
print(type(liste))
for a in liste:
    print(a)
