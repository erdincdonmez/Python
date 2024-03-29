# threshold - 4 THRESH bir arada
import cv2

r = cv2.imread("images/yesil_elma_1.jpg")
r1 = cv2.imread("images/yesil_elma_1.jpg", 0)

gen, yuk, renk = r.shape
rx = cv2.resize(r1, (gen//2,yuk//2))

print(f"Resmin genisliği:{gen}, yüksekliği:{yuk}, rengi:{renk}")

g, y = gen//4, yuk//4
cv2.imshow("Orjinal1", rx)
cv2.waitKey(3000)
cv2.destroyAllWindows()

r1_ = cv2.resize(r1, (gen//4,yuk//4))
for a in range(255):
    _, c1 = cv2.threshold(r1_, a, 255, cv2.THRESH_BINARY)
    _, c2 = cv2.threshold(r1_, a, 255, cv2.THRESH_BINARY_INV)
    _, c3 = cv2.threshold(r1_, a, 255, cv2.THRESH_TOZERO)
    _, c4 = cv2.threshold(r1_, a, 255, cv2.THRESH_TOZERO_INV)
    
    rx[:g, :y] = c1[:, :]
    rx[:g, y:y*2] = c2[:, :]
    rx[g:, :y] = c3[:, :]
    rx[g:, y:y*2] = c4[:, :]
    cv2.imshow("Son şekli", rx)

    cv2.waitKey(10)
 
cv2.waitKey(0)
cv2.destroyAllWindows()









