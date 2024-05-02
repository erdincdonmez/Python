# search işlemi
import re

txt = "Ahmet al renkli bir şal aldı."
x = re.search("al", txt)
print(x) # al ifadesi için dönüş nesnesi
print(x.span()) # al ifadesinin yeri
print(x.span()[0]) # al ifadesinin başı

a = re.search(r"\bş\w+", txt) # ş harfiyle başlayan bir kelime
print(a.span())

x = re.search(r"\bş\w+", txt) # ş ile başlıyorsa al.
print(x.string)

x = re.search(r"\bş\w+", txt) # ş ile başlayan kelimeyi al.
print(x.group())

