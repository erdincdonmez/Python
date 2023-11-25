from datetime import date

# date nesnesi bu günün tarihini içerir
today = date.today() 

print("Yıl:", today.year)
print("Ay :", today.month)
print(type(today.month))
print(today.month+3)
print("Gün:", today.day)

#-----------
from datetime import time

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)
