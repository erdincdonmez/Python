import mysql.connector
try:
  mydb = mysql.connector.connect(
    host="localhost", # default olanı localhost.
    user="root", # default olanı root.
    password="1234" # MySQL WorkBench kurarken yazdığınız şifre
  )
  print("Bağlantı tamam:")
  print(mydb)
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE pythondersleri")
    print("Veritabanı oluşturuldu.")
  except mysql.connector.Error as hata:
    print(f"Veri tabanı oluşturulamadı. Hata : {hata}")
except:
  print("İşlem sırasında bir hata oluştu.")
