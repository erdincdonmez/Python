from datetime import date

# date nesnesi bu günün tarihini içerir
today1 = date.today() 

print("Yıl:", today1.year)
print("Ay :", today1.month)
print("Gün:", today1.day)

yil = int(input ("Doğum yılın nedir?"))
print ("Sen :", today1.year-yil,"yaşındasın.")
print ("Sen :", (today1.year-yil)*12,"ay yaşamışsın.")
print ("Sen :", (today1.year-yil)*365,"gün yaşamışsın.")
