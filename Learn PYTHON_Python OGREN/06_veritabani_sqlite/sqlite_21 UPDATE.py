# OFSET
import sqlite3
veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

secilenvt.execute("SELECT * FROM ogrenciler") 
veri = secilenvt.fetchall()
for aa in veri:
    print(aa)

aranan = "Berkay ÜNLÜ"; yenisi = "Berkay ÜNSÜZ"
secilenvt.execute(f"UPDATE ogrenciler SET ad = '{yenisi}' WHERE ad = '{aranan}'")
veriTabani.commit()

secilenvt.execute("SELECT * FROM ogrenciler") 
veri = secilenvt.fetchall()
for aa in veri:
    print(aa)




veriTabani.close()