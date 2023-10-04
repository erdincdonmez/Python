import os
abc = open("rehber.txt", "w")
# print(os.getcwdb())
print(os.getcwd())
abc.write("Dosyaya kaydedilen veri.\nİkinci satıra geçtik!!\n")
abc.write("Üçüncü satır çalışmaya devam--")
abc.write("!!!\n\n\n")
abc.close()
