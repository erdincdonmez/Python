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
  ('Erhan KARA', '66425236587'),
  ('Burak MERT', '66325214587'),
  ('Alper TOY', '66364125896'),
  ('Ensar GÜL', '66415236541'),
  ('Irmak SAKA', '66426324156'),
  ('Aydın AKA', '66336254158'),
  ('Enes BOZ',  '66465287412'),
  ('Eren SOLAK',  '66075368541'),
  ('Halil Cem AK', '66326325412'),
  ('Yiğit GÜLLÜ',  '66336335241'),
  ('Berkay ÜNLÜ', '66236982544'),
  ('Esma SARI',   '66085236541'),
  ('Arda DOĞRU',   '66436589562'),
  ('Ahmet YOLCU',  '66095236521')
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "kayıt eklendi.")
