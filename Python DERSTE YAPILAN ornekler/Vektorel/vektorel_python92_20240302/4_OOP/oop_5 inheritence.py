class Ilan:
    ilanNo = "tanımsız"
    aciklama = "tanımsız"
    def __init__(self, no):
        self.ilanNo = no

class Araba(): pass


print(Ilan.ilanNo)
ilan1 = Ilan (123)
ilan2 = Ilan (254)

print(ilan1.ilanNo)
print(ilan2.ilanNo)


ilan3 = Araba(658)
ilan4 = Araba(659)
print(ilan1.ilanNo)
print(ilan2.ilanNo)
