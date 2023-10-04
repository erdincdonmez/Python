import os
abc = open("rehber.txt", "w")
# print(os.getcwdb())
print(os.getcwd())
os.chdir(os.getcwd()+"\\Python DERS ICIN ORNEKler\\03_python_dosya_islemleri_8saat")
abc.write("Dosyaya kaydedilen veri.\nİkinci satıra geçtik!!\n")
abc.write("Üçüncü satır çalışmaya devam--")
abc.write("!!!-\n\n\n")
abc.close()
