import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture('test.mp4')
while cap.isOpened():
    ret, frame = cap.read()

    # resize ====================

    img = frame
    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
      
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    frame = resized

    # main part =================

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # countours
    edged = cv.Canny(gray, 30, 200)
    contours, hierarchy = cv.findContours(edged, \
    cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(frame, contours[0:7], -1, (0, 255, 0), 1)

    # rectangles
    for cnt in contours[0:3]:
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow('Contours', frame)

    # =========================== 

    # makes video slower
    time.sleep(0.1)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()