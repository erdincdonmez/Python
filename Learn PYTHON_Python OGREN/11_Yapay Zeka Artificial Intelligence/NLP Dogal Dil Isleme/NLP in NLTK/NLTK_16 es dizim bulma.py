import nltk
# nltk.download("book") # 
from nltk.book import *
from nltk.stem import WordNetLemmatizer

esDizimler = text8.collocations()
print("\n\nEş dizimleri:\n",esDizimler)

# from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in text8]

new_text = nltk.Text(lemmatized_words)
esDizimler = new_text.collocations()
print("\n\nLemmatize edilmiş kelimelerin eş dizimleri:\n",esDizimler)


