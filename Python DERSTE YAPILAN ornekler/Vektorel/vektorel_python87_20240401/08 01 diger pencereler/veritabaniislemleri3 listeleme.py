import sqlite3

xxx = sqlite3.connect("rehber.db")

secilenvt = xxx.cursor()

# secilenvt.execute("CREATE TABLE IF NOT EXISTS kisiler(adSoyad, no)")

##ad = input("Ad soyad :")
##no = input("Telefon  :") 
##secilenvt.execute("INSERT INTO kisiler (adSoyad, no) VALUES('CAN AL','2563254854')")
# secilenvt.execute(f"INSERT INTO kisiler (adSoyad, no) VALUES('{ad}','{no}')")


##xxx.commit()

veriler = secilenvt.execute("SELECT * FROM kisiler") # tüm kayıtlar
##veriler = secilenvt.execute("SELECT * FROM kisiler WHERE adSoyad='CAN AL'") # adSoyad ... olanlar
##veriler = secilenvt.execute("SELECT * FROM kisiler WHERE adSoyad LIKE '%U%'") # içeren
##veriler = secilenvt.execute("SELECT * FROM kisiler WHERE adSoyad LIKE 'M%'") # .. ile başlayan
##veriler = secilenvt.execute("SELECT * FROM kisiler WHERE adSoyad LIKE '%L'") # .. ile biten
##print(veriler)
for a in veriler:
    print(a)
