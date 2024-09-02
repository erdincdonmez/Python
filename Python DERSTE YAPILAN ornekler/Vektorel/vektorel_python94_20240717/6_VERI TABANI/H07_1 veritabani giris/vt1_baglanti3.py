import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    # database="pythondersleri"
    )

    print ("Bağlantı başarılı")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE pythondersleri")

except mysql.connector.Error as hata:
    print (f"İşlem başarısız. Hata: {hata}")


