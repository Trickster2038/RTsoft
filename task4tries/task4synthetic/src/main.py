import cv2 as cv
import numpy as np
import time

print("hello from CV app")

rgb = np.zeros((800,800,3), np.uint8)

cv.circle(rgb,(447,63), 63, (0,127,255), -1)
cv.rectangle(rgb,(384,200),(510,500),(64,255,255),-1)
cv.ellipse(rgb,(256,256),(100,50),0,0,360,(64,127,127),-1)

frame = rgb

# resize ====================

img = frame
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

frame = resized

# main part =================

gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

# countours
edged = cv.Canny(gray, 30, 200)
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(frame, contours[0:7], -1, (0, 255, 0), 1)

# rectangles
for cnt in contours[0:5]:
    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
cv.imshow('Contours', frame)

# print(contours)

# =========================== 

cv.waitKey(0)

cv.destroyAllWindows()

print("buy from CV app")