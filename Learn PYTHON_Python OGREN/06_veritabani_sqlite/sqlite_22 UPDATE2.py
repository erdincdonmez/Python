# OFSET
import sqlite3
veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

secilenvt.execute("SELECT * FROM ogrenciler") 
veri = secilenvt.fetchall()
for aa in veri: print(aa)

aranan = "Ahmet YOLCU"; yenisi = "Ahmet YOL"
sql = "UPDATE ogrenciler SET ad = ? WHERE ad = ?"
val = (yenisi, aranan)
secilenvt.execute(sql, val)
veriTabani.commit()

secilenvt.execute("SELECT * FROM ogrenciler") 
veri = secilenvt.fetchall()
for aa in veri: print(aa)




veriTabani.close()