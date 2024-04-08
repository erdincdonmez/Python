# LIMIT
import sqlite3

veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

secilenvt.execute("SELECT * FROM ogrenciler LIMIT 2 OFFSET 5") # 5'ten itibaren 4 tanesi
secilenvt.execute("SELECT * FROM ogrenciler LIMIT 2 OFFSET 5") # 5'ten itibaren 4 tanesi

veri = secilenvt.fetchall()
for aa in veri:
    print(aa)

veriTabani.close()