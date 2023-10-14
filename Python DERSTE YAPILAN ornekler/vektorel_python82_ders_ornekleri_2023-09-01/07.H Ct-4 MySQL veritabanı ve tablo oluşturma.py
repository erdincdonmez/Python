import mysql.connector
try:
  mydb = mysql.connector.connect(
    host="localhost", # Community Server yerel bilgisayara kurulup çalıştırılmışsa localhost olacak.
    user="root", # MySQL Community Server indirip kurunca özel bir kullanıcı adı verilmemişse root olacak
    password="1234" # MySQL Community Server kurulumu aşamasında size sorduğu şifre
  )
  print("Bağlantı tamam:")
  print(mydb)
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE pythondersleri")
    print("Veritabanı oluşturuldu.")
  except:
    print(f"Veri tabanı oluşturulamadı. Hata : {mysql.connector.Error}")

except:
  print("İşlem sırasında bir hata oluştu.")
