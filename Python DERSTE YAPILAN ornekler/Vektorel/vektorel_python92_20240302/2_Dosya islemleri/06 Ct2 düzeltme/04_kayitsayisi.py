import ast
dosya = open("rehber.txt","r")
print("╠════════╣ KİŞİ EKLEME ╠════════╣")

kayitSayisi = dosya.read()
cevirilen = ast.literal_eval(kayitSayisi)
print(f"Veri {len(cevirilen)+1}.kayit olarak eklendi")

dosya.close()