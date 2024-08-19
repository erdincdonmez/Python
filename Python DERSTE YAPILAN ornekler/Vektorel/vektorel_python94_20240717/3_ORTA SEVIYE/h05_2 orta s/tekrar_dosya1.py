ad = input("Adınız nedir?")
dosya = open("Merhaba"+ad+".py","w")
yazilacakbilgi='print("Merhaba "+ad+"\\nBu python programi virusler gibi otomatik olusturuldu.")\ninput()'
dosya.write('print("Merhaba '+ad+'\\nBu python programi virusler gibi otomatik olusturuldu.")\ninput()')
dosya.close()
