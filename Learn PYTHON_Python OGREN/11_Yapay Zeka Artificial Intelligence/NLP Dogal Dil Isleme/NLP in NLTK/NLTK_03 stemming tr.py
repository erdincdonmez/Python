import nltk
# nltk.download('punkt') # Bir kere yapılması gerek/yeter
from nltk.tokenize import sent_tokenize, word_tokenize

ornek_metin = """Parayı Veren Düdüğü Çalar
Çocuklar, pazara gelen Nasreddin Hoca'nın etrafını sarmış. “Hoca, bana düdük al!” demiş biri. “Bana da, bana da!” demiş bir diğeri.
Diğerleri de sırayla:
– Ben de düdük isterim!
– Bir tane de bana!, demişler.
İçlerinden sadece biri Nasreddin Hoca’ya düdük parası vermiş. Hoca, parayı alıp pazara gitmiş.
Hoca, akşam pazardan dönünce çocuklar etrafını sarmış. Her biri düdüğünü istemiş. Cebinden bir düdük çıkaran hoca, parayı veren çocuğa vermiş.
Diğer çocuklar hep bir ağızdan bağırmış:
– Hani bizim düdüğümüz?
Nasrettin Hoca gülerek,
– Parayı veren düdüğü çalar, demiş.."""

cumleler = sent_tokenize(ornek_metin)
kelimeler = word_tokenize(ornek_metin)

# print(cumleler)
# print("Kelime listesi: ",kelimeler)

# nltk.download("stopwords") # Bir kere indirilmesi gerek/yeterli
from nltk.corpus import stopwords

stop_words_tr = set(stopwords.words("turkish")) # stop word = köksüz/anlamsız kelimeler
temizlenmis_liste = []
print("Stop words Türkçe:",stop_words_tr)

for kelime in kelimeler:
   if kelime.casefold() not in stop_words_tr: # casefold ile küçükharfe çevir.
        temizlenmis_liste.append(kelime)
        
print("Temizlenmiş liste: ",temizlenmis_liste)

# from nltk.stem import PorterStemmer
# stemmer = PorterStemmer()
# kok_cikarilmis_liste = [stemmer.stem(kelime) for kelime in temizlenmis_liste]

# pip install snowballstemmer
from snowballstemmer import TurkishStemmer
turkStem=TurkishStemmer()
# turkStem.stemWord("ekmekler") #ekmek

kok_cikarilmis_liste = [turkStem.stemWord(kelime) for kelime in temizlenmis_liste]

print("Kökleri çıkarılmış liste:",kok_cikarilmis_liste)