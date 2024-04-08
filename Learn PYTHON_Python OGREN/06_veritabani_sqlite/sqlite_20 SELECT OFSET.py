# OFSET
import sqlite3

veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

# secilenvt.execute("SELECT * FROM ogrenciler") # Hepsi
# VVV 4'ten başlayarak (4 dahil) 5 tanesi. 1.kayıt indisi 0
secilenvt.execute("SELECT * FROM ogrenciler LIMIT 5 OFFSET 3") 

veri = secilenvt.fetchall()
for aa in veri:
    print(aa)

veriTabani.close()