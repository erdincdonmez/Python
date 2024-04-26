import sqlite3

xxx = sqlite3.connect("okul.db")
yyy = sqlite3.connect("rehber.db")

secilenOkul = xxx.cursor()
secilenRehber = xxx.cursor()

# secilenOkul.execute("CREATE TABLE ogrenciler(adSoyad, tc)")
secilenOkul.execute("CREATE TABLE IF NOT EXISTS ogrenciler(adSoyad, tc)")
secilenOkul.execute("INSERT INTO ogrenciler (adSoyad, tc) VALUES('CAN AL','2563254854')")
xxx.commit()

