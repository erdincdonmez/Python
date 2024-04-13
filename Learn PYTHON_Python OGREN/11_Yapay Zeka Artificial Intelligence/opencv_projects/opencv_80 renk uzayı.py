cv2'de renk uzayları
import cv2

for a, fonk in enumerate(dir(cv2)): 
    # içinde "COLOR_" ifadesi geçen fonksiyonlar
    if "COLOR_" in fonk : print(a, fonk)

# _ = 12 ; print (_)

# for x in ("Nar","Muz","Kiraz","Dut"):
#     if "a" in x: print (x)