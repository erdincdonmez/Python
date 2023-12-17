import mysql.connector

try:
  # dosya = open("deneme.dat","w")
  veritabani = mysql.connector.connect(host="localhost",user="root",password="1234")
  mydb = mysql.connector.connect(
    host="localhost", # Community Server yerel bilgisayara kurulup çalıştırılmışsa localhost olacak.
    user="root", # MySQL Community Server indirip kurunca özel bir kullanıcı adı verilmemişse root olacak
    password="1234" # MySQL Community Server kurulumu aşamasında size sorduğu şifre
  )
  print("Bağlantı tamam:")
  print(mydb)
  print(veritabani)
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE eticaret")
    print("Veritabanı oluşturuldu.")
  except:
    print(f"Veri tabanı oluşturulamadı. Hata : {mysql.connector.Error}")

except mysql.connector.Error as hata:
  print(f"Veri tabanı bağlantısı oluşturulamadı. Detay : {hata}")
