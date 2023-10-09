#sozluk = {"fil":"elephand","aslan":"lion","köpek":"dog"}
#print(sozluk)
#print(sozluk["aslan"])

rehber = {"Yiğit":"5078956854","Halil":"0544625478","Eren":"5095622458"}
print(rehber)
print ("Kayıt sayısı:",len(rehber))

"""
rehber["Yiğit"] = "5336325987"
print(rehber)
print ("Kayıt sayısı:",len(rehber))

rehber.update({"Erdinc": "214"})
print(rehber)
print ("Kayıt sayısı:",len(rehber))

print(rehber["Yiğit"])

rehber.pop("Eren")
print(rehber)
"""
for kisi in rehber:
    print(kisi,rehber[kisi])
