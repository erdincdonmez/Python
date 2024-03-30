# not1=5
# with open("deneme1.txt","a") as xx:
#     xx.write("\nMerhaba\n")
#     xx.write(f"Puan:{not1}")

try:
    okunan = open("deneme1.txt","r")
    print(okunan)
    okunan.close()
except:
    print("Bir hata oluştu.")
