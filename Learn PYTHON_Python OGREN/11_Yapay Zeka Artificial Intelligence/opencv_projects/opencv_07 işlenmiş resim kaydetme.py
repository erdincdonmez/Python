# İşlenmiş resmi kaydetmeimport cv2
img = cv2.imread('images/square1.jpg',0)
tus = cv2.waitKey(0)
cv2.imwrite('images/square1.jpg',img)
cv2.destroyAllWindows()
