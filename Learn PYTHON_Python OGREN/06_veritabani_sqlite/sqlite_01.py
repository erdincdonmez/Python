# Kaynak: https://python-istihza.yazbel.com/standart_moduller/sqlite.html 
import sqlite3
# import sqlite3 as sql # şeklinde de kullabilirsiniz.
# import sqlite3 as lite # şeklinde de kullabilirsiniz.

# Bu adreslerden örnek bir veritabanı indirin.
# chinook.db https://www.sqlitetutorial.net/sqlite-sample-database/
# kitaplar.sqlite https://en.wikiversity.org/wiki/Database_Examples/Northwind/SQLite

vt = sqlite3.connect('kitaplar.sqlite') # varsa bağlan, yoksa oluştur.

# RAM üzerinde bir veritabanı bağlantısı oluştur
# vt = sqlite3.connect(":memory:")


vt.commit() # Değişiklikleri kabul et/kaydet

vt.close() # Veritabanı bağlantısını kapat