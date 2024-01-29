dosya = open("rehber2.txt","r")
print("╔════════════════════════════╗")
print("║  Kayıtlı kişiler           ║")
print("╚════════════════════════════╝")

##okunan = dosya.readlines()
####print(okunan)
##for a in okunan:
##    print(dict(a))
    
okunan = dosya.read()
##print(okunan)
for a in okunan:
    print(dict(a))
##    b=dict(a)
##    print(dict(b["adi"]))
##for a in okunan:
##    print(dict(a))

dosya.close()

