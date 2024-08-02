not1 = int(input("Ortalaman kaç?"))
if not1<0 or not1>100: print("Yanlış giriş yaptın")
else: 
    if not1>90: print("Süpersin")
    elif 70>not1>60  : print("idare eder.")
    elif not1>50: print("geçtin")