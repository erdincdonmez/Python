# cv2'de renkleri ayırma
import cv2

img = cv2.imread('images/top1_32x32_1.png')
# img = cv2.imread('images/ornekresim01_150x100.png')

m, y, k = cv2.split(img)
boy, en, _ = img.shape
print(k.shape)
print("   ",end="")
for j in range(en): print(f"{j}{' '*(2-len(str(j)))}", end="")
print("\n  ","_"*(en*2-2))

for i in range(en):
    print(f"{i}{" "*(2-len(str(i)))}:",end="")
    for j in range(en):
        # print(k[i][j]," "*(3-len(str(k[i][j]))), end="")
        # if k[i][j] > 70: print("X ", end="") # kırmızı renk değeri yüksek olanlar
        # if k[i][j] > 150 and m[i][j] < 100 and y[i][j] < 100: print("X ", end="") # muhtemel kırmızı alanlar
        if k[i][j] > 200 and m[i][j] > 200 and y[i][j] > 200: print("X ", end="") # muhtemel beyaz alanlar
        else: print("  ", end="") 
    print()

cv2.waitKey(0)
cv2.destroyAllWindows()
