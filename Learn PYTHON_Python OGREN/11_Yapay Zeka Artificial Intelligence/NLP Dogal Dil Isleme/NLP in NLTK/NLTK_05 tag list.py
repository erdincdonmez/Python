import nltk

try: nltk.data.find('help/tagsets') # yoksa downlad et.
except LookupError: nltk.download('tagsets')

print("\n\nNLTK Tag listesi:\n")
nltk.help.upenn_tagset()