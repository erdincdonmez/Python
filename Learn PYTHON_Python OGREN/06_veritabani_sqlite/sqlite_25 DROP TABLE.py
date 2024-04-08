# DROP TABLE
import sqlite3
veriTabani = sqlite3.connect('okultakipsistemi.db') 
secilenvt = veriTabani.cursor()

# secilenvt.execute("DROP TABLE ogrenciler1") # yoksa hata verir
secilenvt.execute("DROP TABLE IF EXISTS ogrenciler1") 

veriTabani.close()