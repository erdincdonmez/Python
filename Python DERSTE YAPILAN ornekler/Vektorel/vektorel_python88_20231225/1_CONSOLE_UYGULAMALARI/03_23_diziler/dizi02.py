import random
corba = ["Tarhana","Yayla","Ezo gelin"]
anaYemek = ["Karnı yarık","Kuru fasülye","Mantı"]
icecek = ["Ayran","Kola","Gazoz"]

print("Menü Öneri Programı")
print(f"Bu gün size {random.choice(corba)} çorbası,")
print(f"{random.choice(anaYemek)} yemeği,")
print(f"ve {random.choice(icecek)} öneriyorum.")

