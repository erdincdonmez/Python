import mysql.connector
try:
  VeriTabani1 = mysql.connector.connect(
    host="localhost", # default olanı localhost.
    user="root", # default olanı root.
    password="1234" # MySQL WorkBench kurarken yazdığınız şifre
  )
  secilenVT = VeriTabani1.cursor()
  secilenVT.execute("CREATE DATABASE pythondersleri")
  print("Veritabanı oluşturuldu.")
except:
  print("İşlem sırasında bir hata oluştu.")
