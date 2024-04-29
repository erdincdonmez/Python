import re
metin1 = "Bugün hava çok soğuk"
metin2 = "Bursa çok sıcak"
metin3 = "Bugün hava soğuk."

aranan = "^Bu.*sıcak$" # Başında Bu olan ve sıcak ile biten
print(re.search(aranan, metin1))
print(re.search(aranan, metin2))
print(re.search(aranan, metin3))