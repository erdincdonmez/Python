konu = "not hesaplama programı"
print (konu)
print ("_"*len(konu))

not1 = int(input("Matematik ortalaman kaç? "))
if not1 > 70 and not1<=100:
    print("çok iyi")
elif not1 > 49 and not1<=100:
    print ("Geçtin")
elif not1 <= 49 and not1>0:
    print("Kaldın")
else :
    print ("böyle not olmaz")