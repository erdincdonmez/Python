# fetchone
import sqlite3

veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

def verileriAlSatirSatirYaz():
    aranan = "Esma SARI"
    secilenvt.execute(f"SELECT * FROM ogrenciler WHERE ad = '{aranan}'")
    veri = secilenvt.fetchall()
    print(veri)

verileriAlSatirSatirYaz()
veriTabani.close()