import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost", # Community Server yerel bilgisayara kurulup çalıştırılmışsa localhost olacak.
    user="root", # MySQL Community Server indirip kurunca özel bir kullanıcı adı verilmemişse root olacak
    password="1234" # MySQL Community Server kurulumu aşamasında size sorduğu şifre
  )
  print("Bağlantı tamam:")
  print(mydb)
except:
  print("Veri tabanına bağlanırken bir hata oluştu.")



# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")