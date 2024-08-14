# ör-2: Dosya oluşturma xxxxxxxxxxxxxxxx
abc = open("rehber.txt", "w")
#abc = open("rehber.txt", "a")
# abc = open("d:\\rehber.txt", "a")
abc.write("Dosyaya kaydedilen veri.\nİkinci satır!!\n")
abc.write("Üçüncü satır") 
abc.write("Dördüncü satır") 
abc.close() # oluşturulan her dosya kapatılmalıdır.
