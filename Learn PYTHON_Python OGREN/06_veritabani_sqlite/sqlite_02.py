# Kaynak: https://python-istihza.yazbel.com/standart_moduller/sqlite.html 
import sqlite3
# import sqlite3 as sql # şeklinde de kullabilirsiniz.
# import sqlite3 as lite # şeklinde de kullabilirsiniz.

# Bu adreslerden örnek bir veritabanı indirin.
# chinook.db https://www.sqlitetutorial.net/sqlite-sample-database/
# kitaplar.sqlite https://en.wikiversity.org/wiki/Database_Examples/Northwind/SQLite

vt = sqlite3.connect('kutuphane.sqlite') # varsa bağlan, yoksa oluştur.

# RAM üzerinde bir veritabanı bağlantısı oluştur
# vt = sqlite3.connect(":memory:")

# Hangi veritabanı ile çalışacağını, veritabanını seçer.
cursor = vt.cursor()

# Kitaplar tablosunu oluştur
cursor.execute('''CREATE TABLE kitaplar (
                    id INTEGER PRIMARY KEY,
                    baslik TEXT NOT NULL,
                    yazar TEXT NOT NULL,
                    yayin_tarihi DATE
                )''')

# Veritabanı işlemleri gerçekleştirebilirsiniz. Örneğin, kitap ekleme:
cursor.execute("INSERT INTO kitaplar (baslik, yazar, yayin_tarihi) VALUES (?, ?, ?)", ("Deneme Kitabı", "Bir Yazar", "2024-01-01"))

vt.commit() # Değişiklikleri kabul et/kaydet

vt.close() # Veritabanı bağlantısını kapat