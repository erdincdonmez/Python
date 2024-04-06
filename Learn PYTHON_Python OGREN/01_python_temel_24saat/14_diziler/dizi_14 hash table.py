# Hash table
# Hafızada gerektiği kadar (dinamik) yer ayrılır ve gerektikçe büyür, küçülür
# Hafızada hızlı erişimi sağlar
dizi = {}
dizi ['adi'] = "Erdinç"
dizi ['soyadı'] = "Dönmez"
print (dizi)
print("dizi.keys()  : ",dizi.keys())
print("dizi.items() : ",dizi.items())
print("dizi.values(): ",dizi.values())

if 'adi' in dizi: print('adi var') 
else: print('adi yok')

if 'numarasi' in dizi: print('numarasi var') 
else: print('numarasi yok')

print('adi      : ',dizi['adi'])
# print('numarasi : ',dizi['numarasi']) # hata verir

print('adi      : ',dizi.get('adi'))
print('numarasi : ',dizi.get('numarasi')) # hata vermez

dizi['c']='E'
print(dizi)
print(dizi.keys())
print(dizi.values())
print(sorted(dizi.values()))