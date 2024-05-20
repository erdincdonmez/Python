import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

try: nltk.find('tokenizers/punkt') # yoksa downlad et.
except LookupError: nltk.download('punkt')
try: nltk.find('averaged_perceptron_tagger')
except: nltk.download('averaged_perceptron_tagger') 

ornek_metin = """
'Twas brillig, and the slithy toves did gyre and gimble in the wabe:
all mimsy were the borogoves, and the mome raths outgrabe."""

kelimeler = word_tokenize(ornek_metin)


print("\nEtiketlenmiş kelimeler: ",nltk.pos_tag(kelimeler))

