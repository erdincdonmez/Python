from datetime import *
print("Bugün:", date.today())

tamTarih = datetime.now()
print("Şimdi =", tamTarih, type(tamTarih))

tamTarihStr = str(tamTarih)
print("Şimdi =", tamTarihStr, type(tamTarihStr))
print(tamTarihStr[0:4])

buyil=int(tamTarihStr[0:4])
print(buyil-1995,"yıl yaşamışsın.")
print((buyil-1995)*365,"gün yaşamışsın.")