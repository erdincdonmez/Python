import datetime

simdikiYil = datetime.date.today().year
print("Yıl:", simdikiYil )

dogumYili = int(input("Doğduğun yıl nedir?"))

yasadigiYil = simdikiYil - dogumYili

print (yasadigiYil,"yaşındasın demek.")
