
from datetime import date

today = date.today()
print ("Today: ",today)
# dd/mm/YY
cevrilmisToday = today.strftime(" %d - %m -%Y-%B-%y")
print("Çevrilmiş şekli =", cevrilmisToday, type(cevrilmisToday))

gun = today.strftime("%d")
ay = today.strftime("%m")
print("Gün: ",gun)
print("Ay: ",ay)
x = 14
print(x,"ay sonra:",(int(ay)+x)%12)