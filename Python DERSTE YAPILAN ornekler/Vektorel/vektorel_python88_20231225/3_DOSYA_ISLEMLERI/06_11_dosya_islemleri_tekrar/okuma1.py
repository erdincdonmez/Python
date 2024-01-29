dosya = open("rehber.txt","r")
print("╔════════════════════════════╗")
print("║  Kayıtlı kişiler           ║")
print("╚════════════════════════════╝")

##for a in range(5):
##    okunan = dosya.read(5)
##    print(okunan)

okunan = dosya.readlines()
##print(okunan)
for a in okunan:
    print(a)

dosya.close()

##for b in dosya:
##    print(dosya.readline())
