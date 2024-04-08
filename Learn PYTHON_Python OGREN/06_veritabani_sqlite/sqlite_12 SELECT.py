# DATE TIME
import sqlite3, datetime, time, random

veriTabani = sqlite3.connect('okultakipsistemi.db') # varsa bağlan, yoksa oluştur.
secilenvt = veriTabani.cursor()

def verileriAlSatirSatirYaz():
    secilenvt.execute("SELECT ad, tel FROM ogrenciler")
    veri = secilenvt.fetchall()
    for satir in veri:
        print(satir)

# tabloOlustur()
# kayitEkleme()
# kayitEklemeTarihSaatile()
# cokluEkleme()
# verileriAl()
verileriAlSatirSatirYaz()
veriTabani.close()


# # ör-4: verilerin tümünü al
# myresult = mycursor.fetchall()

# # ör-5: verilerden bir tane al
# myresult = mycursor.fetchone()

# # ör-6: adı birşey olanları al
# sql = "SELECT * FROM ogrenciler WHERE ad = "Esma SARI", )

# mycursor.execute(sql, aranan)
# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
