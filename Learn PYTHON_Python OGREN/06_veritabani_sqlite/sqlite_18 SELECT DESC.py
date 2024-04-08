# LIKE
import sqlite3

veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

secilenvt.execute("SELECT * FROM ogrenciler") # Sıralamasız
secilenvt.execute("SELECT * FROM ogrenciler ORDER BY ad ASC") # A-Z sıralı
secilenvt.execute("SELECT * FROM ogrenciler ORDER BY ad DESC") # Testen sıralı
veri = secilenvt.fetchall()
for aa in veri:
    print(aa)

veriTabani.close()