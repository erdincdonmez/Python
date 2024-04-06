
not1=5
with open("deneme/sayilar.txt","a") as xx:
    for a in range(10):
        # xx.write(a) # dosyaya int yazılamaz
        # xx.write(str(a))
        xx.write(f"\n{a}")
