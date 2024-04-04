import cv2

cam = cv2.VideoCapture(0)

print(cam.get(3)) # WIDTH
print(cam.get(4)) # HEIGHT

cam.set(3,100) 
cam.set(4,200)

print("W: ",cam.get(3))
print("H: ",cam.get(4))

print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))