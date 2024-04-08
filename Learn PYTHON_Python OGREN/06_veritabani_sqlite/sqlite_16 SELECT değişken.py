# Değişken ile SQL komutları
import sqlite3

veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

def veriAl():
    sqlkomutu = "SELECT * FROM ogrenciler WHERE ad = ?"
    aranan = ("Esma SARI",)

    secilenvt.execute(sqlkomutu, aranan)
    veri = secilenvt.fetchall()
    print(veri)

veriAl()
veriTabani.close()