##open("rehber.txt","w")
##open("rehber.txt","w").write("Deneme")

for a in range(10):
    dosya = open(f"rehber{a}.txt","w")
    dosya.write("Deneme1")
    dosya.close()
