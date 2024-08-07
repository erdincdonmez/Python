from datetime import date

# date nesnesi bugünün tarihini içerir
# today = date.today() 

# print("Yıl:", today.year)
# print("Ay :", today.month)
# print("Gün:", today.day)

print("Yıl:", date.today().year)
print("Ay :", date.today().month)
print("Gün:", date.today().day)

yil = int(input ("Doğum yılın nedir?"))
print ("Sen :", date.today().year-yil,"yaşındasın.")
# print ("Sen :", (today.year-yil)*12,"ay yaşamışsın.")
# print ("Sen :", (today.year-yil)*365,"gün yaşamışsın.")
