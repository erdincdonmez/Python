import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

try: nltk.find("taggers/averaged_perceptron_tagger") # yoksa downlad et.
except LookupError: nltk.download('averaged_perceptron_tagger')


ornek_metin = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""
ornek_metin = "I'm Erdinch and I'm working as a teacher"
ornek_metin = "It's a dangerous business, Frodo, going out your door."

words_in_lotr_quote = word_tokenize(ornek_metin)

lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
print("lotr_pos_tags : ",lotr_pos_tags)

grammar = """Chunk: 
{<.*>+}
}<JJ>{"""
chunk_parser = nltk.RegexpParser(grammar)

tree = chunk_parser.parse(lotr_pos_tags)
print("\n\ntree:\n",tree)
tree.draw() 