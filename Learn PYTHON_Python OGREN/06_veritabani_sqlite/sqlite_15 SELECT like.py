# LIKE
import sqlite3

veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

def verileriAlSatirSatirYaz():
    aranan = "er"
    secilenvt.execute(f"SELECT * FROM ogrenciler WHERE ad LIKE '%{aranan}%'") # içinde .. geçenler
    # secilenvt.execute(f"SELECT * FROM ogrenciler WHERE ad LIKE '{aranan}%'") # .. ile başlayanlar
    # secilenvt.execute(f"SELECT * FROM ogrenciler WHERE ad LIKE '%{aranan}'") # .. ile bitenler
    veri = secilenvt.fetchall()
    print(veri)

verileriAlSatirSatirYaz()
veriTabani.close()