# Değişken ile SQL komutları
import sqlite3

veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

def veriAl():
    aranan = "Esma SARI"
    secilenvt.execute(f"SELECT * FROM ogrenciler WHERE ad = '{aranan}'")
    veri = secilenvt.fetchall()
    print(veri)

veriAl()
veriTabani.close()