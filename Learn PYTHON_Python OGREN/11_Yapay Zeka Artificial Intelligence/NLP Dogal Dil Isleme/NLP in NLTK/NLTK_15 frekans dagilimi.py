# pip install matplotlib
import nltk
# nltk.download("book") # 
from nltk.book import *
import matplotlib.pyplot as plt
from nltk import FreqDist

# en çok kullanılan 20 token
frequency_distribution = FreqDist(text8)
encokKullanilanlar = frequency_distribution.most_common(20)

print(encokKullanilanlar)

# stop_words / manasız kelimelerin olmadığı en çok kullanılan 20 token.
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english")) # stop word = anlamsız kelimeler
meaningful_words = [word for word in text8 if word.casefold() not in stop_words]

frequency_distribution = FreqDist(meaningful_words)
encokKullanilanlar = frequency_distribution.most_common(20)
print(encokKullanilanlar)

# En çok kullanılan 20 kelime grafiği
frequency_distribution.plot(20, cumulative=True)






