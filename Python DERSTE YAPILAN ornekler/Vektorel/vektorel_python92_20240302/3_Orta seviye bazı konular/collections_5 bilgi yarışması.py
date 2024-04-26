#Bu program başkentler bilgi yarışması oyunudur.
import random
Sorular=[
  "Fransa'nın başkenti neresidir?",
  "Çin'in başkenti neresidir?",
  "Japonya'nın başkenti neresidir?",
  "İran'ın başkenti neresidir?",
  "Amerika'nın başkenti neresidir?",
]
DogruCevaplar=[
  "Paris",
  "Pekin",
  "Tokyo",
  "Tahran",
  "Washington",
]

sayiuret=random.randint(0,len(Sorular))

cevap=input(Sorular[sayiuret])

if (cevap==DogruCevaplar[sayiuret]) : print("Bildin")
else : print("Olmadı dostım, puanını kırdım.")
