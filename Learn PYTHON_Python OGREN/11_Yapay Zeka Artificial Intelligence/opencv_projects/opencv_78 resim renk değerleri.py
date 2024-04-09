# cv2'de renkleri ayırma
import cv2

img = cv2.imread('images/top1_32x32_1.png')
# cv2.imshow('Pencere',img)

m, y, k = cv2.split(img)

# cv2.imshow("Maviler     ", m)
# cv2.imshow("Yeşiller    ", y)
# cv2.imshow("Kirmizilar  ", k)

# print(k)

print(k.shape)
print("   ",end="")
for j in range(32): print(f"{j}{' '*(4-len(str(j)))}", end="")
print("\n  ","_"*127)

for i in range(32):
    print(f"{i}{" "*(2-len(str(i)))}:",end="")
    for j in range(32):
        print(k[i][j]," "*(3-len(str(k[i][j]))), end="")
    print()

cv2.waitKey(0)
cv2.destroyAllWindows()
