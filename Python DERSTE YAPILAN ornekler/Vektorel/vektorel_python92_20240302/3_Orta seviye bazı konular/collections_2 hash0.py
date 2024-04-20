# Hash table
# Hafızada gerektiği kadar (dinamik) yer ayrılır ve gerektikçe büyür, küçülür
# Hafızada hızlı erişimi sağlar
dizi = {}
ogrenciler = []
ogrenci ={}
ogrenci1 ={}
# ogrenciler = {
#     {"adi":"Ali", "no":235},
#     {"adi":"Ali", "no":235}
#     }
ogrenci1['adi'] = "Ali"
ogrenci1['no'] = 235
ogrenciler.append(ogrenci1)
ogrenci['adi'] = "Barış"
ogrenci['no'] = 332
ogrenciler.append(ogrenci)
# dizi ['adi'] = "Erdinç"
# dizi ['soyadı'] = "Dönmez"
# print (dizi)
# print("dizi.keys()  : ",dizi.keys())
# print("dizi.items() : ",dizi.items())
# print("dizi.values(): ",dizi.values())
print (ogrenciler)

