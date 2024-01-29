dosya = open("rehber.txt","r")
print("╔════════════════════════════╗")
print("║  Kayıtlı kişiler           ║")
print("╚════════════════════════════╝")

    
okunan = dosya.readlines()
##print(okunan)
for a in okunan:
    print(a)
    b, s = a.split()
    print(b)
    print(s)


dosya.close()

