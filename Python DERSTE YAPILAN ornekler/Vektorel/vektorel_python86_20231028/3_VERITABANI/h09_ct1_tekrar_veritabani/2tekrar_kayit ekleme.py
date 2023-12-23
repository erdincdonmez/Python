import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="vektorel"
)

mycursor = mydb.cursor()

sql = "INSERT INTO ogrenciler (adi, tc) VALUES (%s, %s)"
val = [
  ('Erhan KARA', '85425236587'),
  ('Burak MERT', '85325214587'),
  ('Alper TOY', '85364125896'),
  ('Ensar GÜL', '85415236541'),
  ('Irmak SAKA', '85426324156'),
  ('Aydın AKA', '85336254158'),
  ('Enes BOZ',  '85465287412'),
  ('Eren SOLAK',  '85075368541'),
  ('Halil Cem AK', '85326325412'),
  ('Yiğit GÜLLÜ',  '85336335241'),
  ('Berkay ÜNLÜ', '85236982544'),
  ('Esma SARI',   '85085236541'),
  ('Arda DOĞRU',   '85436589562'),
  ('Ahmet YOLCU',  '85095236521')
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "kayıt eklendi.")
