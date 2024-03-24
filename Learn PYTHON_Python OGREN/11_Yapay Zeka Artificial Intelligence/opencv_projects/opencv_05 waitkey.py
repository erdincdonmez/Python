# waitKey ile tuşu alma
import cv2
img = cv2.imread('images/square1.jpg',0)
cv2.imshow('Deneme',img)
print("kapatmak için a tuşuna basınız")
tus = cv2.waitKey(0)
print("Basılan tuş ascii kodu: ", tus)
# if tus == 97: # a
if tus == ord('a'): # ord('a') anın ascii kodunu verir
    print("a tuşuna basılarak kapatıldı.")

cv2.destroyAllWindows()
