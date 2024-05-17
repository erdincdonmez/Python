import nltk
# nltk.download('punkt') # Bir kere yapılması gerek/yeter
from nltk.tokenize import sent_tokenize, word_tokenize

ornek_metin = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

cumleler = sent_tokenize(ornek_metin)
kelimeler = word_tokenize(ornek_metin)

# print(cumleler)
# print("Kelime listesi: ",kelimeler)

# nltk.download("stopwords") # Bir kere indirilmesi gerek/yeterli
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english")) # stop word = anlamsız kelimeler
# stop_words_tr = set(stopwords.words("turkish")) # stop word = köksüz/anlamsız kelimeler
temizlenmis_liste = []
print("Stop words:",stop_words)
# print("Stop words Türkçe:",stop_words_tr)

for kelime in kelimeler:
   if kelime.casefold() not in stop_words: # casefold ile küçükharfe çevir.
        temizlenmis_liste.append(kelime)
        
print("Temizlenmiş liste: ",temizlenmis_liste)

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

kok_cikarilmis_liste = [stemmer.stem(kelime) for kelime in temizlenmis_liste]

print("Kökleri çıkarılmış liste:",kok_cikarilmis_liste)