
for r in range (5):
    
    dosyaAdi ="vektorel"+str(r+1)+".dat"
    abc = open(dosyaAdi, "w")

    #abc.write(srt(r))
    abc.write("Dosyaya kaydedilen veri.\nİkinci satıra geçtik!!\n")
    abc.write("Üçüncü satır çalışmaya devam--")
    abc.write("!!!xxx\n\n\n")
abc.close()
