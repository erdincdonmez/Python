gun = "cumartesi"
sicaklik = 36
# günlerden cumartesi veya pazar ise ve sıcaklık 30 üzeri ise dışarı çık
"""
if (sicaklik>30 and (gun =="pazar" or gun =="cumartesi")):
    print ("Dışarıya çıkabilirsin")
else: print("Dışarı çıkmak için uygun değil.")
"""
if gun =="cumartesi":
    print ("Hafta sonu")
elif gun =="pazar":
    print ("Hafta sonu")
else:
    print("Hafta içi")