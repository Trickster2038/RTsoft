import numpy as np
import cv2 as cv


cap = cv.VideoCapture('test.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow('frame', gray)
    
    # ================  

    img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY);
    ret,thresh = cv.threshold(img,127,255,0)
    contours,hierarchy = cv.findContours(thresh, 1, 2)
    cnt = contours[0]

    # print(cnt)

    # M = cv.moments(cnt)
    # print( M )

    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    # rect = cv.minAreaRect(cnt)
    # box = cv.boxPoints(rect)
    # box = np.int0(box)
    # cv.drawContours(img,[box],0,(0,0,255),2)
    cv.drawContours(img, contours, -1, (0, 255, 0), 3)

    cv.imshow('frame', img)

    # ================  

    if cv.waitKey(1) == ord('q'):
        break
    while True:
        if cv.waitKey(1) == ord('w'):
            break
        # if cv.waitKey(1) == ord('q'):
        #     raise ValueError("application terminated") 
cap.release()
cv.destroyAllWindows()