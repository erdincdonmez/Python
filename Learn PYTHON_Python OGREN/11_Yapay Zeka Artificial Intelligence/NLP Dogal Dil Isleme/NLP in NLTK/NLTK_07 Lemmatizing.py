import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

try: nltk.find("corpora/wordnet") # yoksa downlad et.
except LookupError: nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves")
ornek_metin = "The friends of DeSoto love scarves."
words = word_tokenize(ornek_metin)

print(f"\n\n{ornek_metin} \niçin kelime lemmaları:")
for kelime in words: print(kelime)

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print(f"\n\nLemmatize edilmiş şekli:")
for kelime in lemmatized_words: print(kelime)

kk = "worst"
print(f"\n{kk} lemması: ",lemmatizer.lemmatize(kk)) # ne olduğunu söylemeyince isim kabul etti
print(f"\nsıfat olarak {kk} lemması: ",lemmatizer.lemmatize(kk, pos="a")) # ikinci parametreyle sıfat dedik 


