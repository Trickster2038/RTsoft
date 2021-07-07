import cv2 as cv
import numpy as np
import time
from collections import deque

print("hello from CV app")

pts = deque(maxlen=124)

cap = cv.VideoCapture('test2.mp4')
while cap.isOpened():
    # print("CV-loop")
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

    contours2 = contours[0:7]

    cv.drawContours(frame, contours2, -1, (0, 255, 0), 1)

    # rectangles
    for cnt in contours2:
        x,y,w,h = cv.boundingRect(cnt)
        if frame.shape[1]/w < 30 and frame.shape[0]/h < 30:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            center=(int(x+w/2),int(y+h/2))
            pts.appendleft(center)

    for i in range(1,len(pts)):
                if pts[i-1]is None or pts[i]is None:
                    continue
                thickness = int(np.sqrt(64 / float(i + 1)) * 1)
                if thickness > 0:
                    cv.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
    cv.imshow('Contours', frame)

    # =========================== 

    # makes video slower
    time.sleep(0.1)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

print("buy from CV app")