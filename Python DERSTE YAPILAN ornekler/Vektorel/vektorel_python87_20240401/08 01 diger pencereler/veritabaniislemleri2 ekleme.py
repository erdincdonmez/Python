import sqlite3

xxx = sqlite3.connect("rehber.db")

secilenvt = xxx.cursor()

secilenvt.execute("CREATE TABLE IF NOT EXISTS kisiler(adSoyad, no)")

ad = input("Ad soyad :")
no = input("Telefon  :") 
#secilenvt.execute("INSERT INTO kisiler (adSoyad, no) VALUES('CAN AL','2563254854')")
secilenvt.execute(f"INSERT INTO kisiler (adSoyad, no) VALUES('{ad}','{no}')")

xxx.commit()

