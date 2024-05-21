import nltk
from nltk.tokenize import word_tokenize

try: nltk.data.find("chunkers/maxent_ne_chunker") # yoksa downlad et.
except LookupError: nltk.download('maxent_ne_chunker')
try: nltk.data.find("corpora/words") # yoksa downlad et.
except LookupError: nltk.download('words')

ornek_metin = """
Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
for countless centuries Mars has been the star of war—but failed to
interpret the fluctuating appearances of the markings they mapped so well.
All that time the Martians must have been getting ready.

During the opposition of 1894 a great light was seen on the illuminated
part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
and then by other observers. English readers heard of it first in the
issue of Nature dated August 2."""

def extract_ne(quote):
    words = word_tokenize(quote, language='english')
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE"
    )

words_in_lotr_quote = word_tokenize(ornek_metin)

lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
print("lotr_pos_tags : ",lotr_pos_tags)

tree = nltk.ne_chunk(lotr_pos_tags)
print("\n\ntree:\n",tree)
tree.draw() 

tree = nltk.ne_chunk(lotr_pos_tags, binary=True)
tree.draw()

print(extract_ne(ornek_metin))