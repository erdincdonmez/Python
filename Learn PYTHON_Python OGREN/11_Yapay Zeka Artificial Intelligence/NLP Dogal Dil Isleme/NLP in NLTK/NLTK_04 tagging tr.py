import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

try: nltk.find('tokenizers/punkt') # yoksa downlad et.
except LookupError: nltk.download('punkt')
try: nltk.find('stopwords') # yoksa downlad et. 
except LookupError: nltk.download('stopwords')
try: nltk.find('averaged_perceptron_tagger') 
except: nltk.download('averaged_perceptron_tagger') 

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

# print("Cümle listesi  : ",cumleler); ; # print("Kelime listesi : ",kelimeler)

from nltk.corpus import stopwords

# stop_words = set(stopwords.words("english")) # stop word = anlamsız kelimeler
# print("Stop words:",stop_words)
stop_words = set(stopwords.words("turkish")) # stop word = köksüz/anlamsız kelimeler
# print("Stop words Türkçe:",stop_words)

temizlenmis_liste = []
for kelime in kelimeler:
   if kelime.casefold() not in stop_words: # casefold ile küçükharfe çevir.
        temizlenmis_liste.append(kelime)        
print("\nTemizlenmiş liste: ",temizlenmis_liste)

# from nltk.stem import PorterStemmer
# stemmer = PorterStemmer()

# kok_cikarilmis_liste = [stemmer.stem(kelime) for kelime in temizlenmis_liste]

# print("\nKökleri çıkarılmış liste:",kok_cikarilmis_liste)

print("\nEtiketlenmiş kelimeler: ",nltk.pos_tag(kelimeler))