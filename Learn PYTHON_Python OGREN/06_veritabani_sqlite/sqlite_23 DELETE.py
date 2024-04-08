# OFSET
import sqlite3
veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

secilenvt.execute("SELECT * FROM ogrenciler") 
veri = secilenvt.fetchall()
for aa in veri: print(aa)

silinecek = "Berkay ÜNSÜZ"
secilenvt.execute(f"DELETE FROM ogrenciler WHERE ad = '{silinecek}'")
veriTabani.commit()

secilenvt.execute("SELECT * FROM ogrenciler") 
veri = secilenvt.fetchall()
for aa in veri: print(aa)

veriTabani.close()