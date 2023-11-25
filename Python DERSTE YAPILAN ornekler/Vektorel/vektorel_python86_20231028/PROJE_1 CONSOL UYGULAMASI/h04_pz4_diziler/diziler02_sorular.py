sorular = [
    "Su neden mavidir?",
    "Eğer bir yarışta ikinci kişiyi geçerseniz kaçıncı olursunuz?",
    "Dayımın tek kız kardeşinin kocası neyin olur?",
    "Soru4"]
cevaplar = [
    "Biz de bilmiyoruz",
    "Birinci",
    "Baban",
    "Cevap4"
]
import random
soru = random.randint(0,len(sorular)-1)
print(sorular[soru])
cevap = input()
if cevap == cevaplar[soru] : 
    print("Bildin.")
else:
    print("Bilemedin.")

