import cv2 as cv
import numpy as np
import time
from collections import deque

def running_mean(x, N):
    """ 
    x == an array of data. 
    N == number of samples per average 
    """
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

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

    # N = len(pts)
    pts_list = list(pts)

    print(pts_list)
    print("===========")

    list_x = []
    list_y = []
    for elem in pts_list:
        #print(list(elem))
        list_x = np.append(list_x, list(elem)[0])
        list_y = np.append(list_y, list(elem)[1])

    # print(list(list_x))
    # pts_list_x = pts_list[:][0]
    # print(pts_list[0])
    # pts_list_y = pts_list[:][1]

    N = 10

    x_avg = running_mean(list_x, min([len(list_x),N]))
    y_avg = running_mean(list_y, min([len(list_y),N]))
    print(x_avg)
    print("________________")
    print(len(pts))
    print(len(x_avg))
    # x_avg = np.convolve(list_x, np.ones(N)/N, mode='valid')
    # y_avg = np.convolve(list_y, np.ones(N)/N, mode='valid')

    # print(x_avg)
    
    pts2 = deque(maxlen=124)

    for i in range(0,len(x_avg)):
        pts2.append((int(x_avg[i]), int(y_avg[i])))
    print(pts2)


    # print(pts)

    # pts_avg_list[:][0] = x_avg
    # pts_avg_list[:][1] = y_avg

    #pts = deque(pts_avg_list)

    #print(pts_list[0])
    #print(pts_list_x[0])
    # pts_list_avg = np.convolve(pts_list, np.ones(N)/N, mode='valid')
    # pts = deque(pts_list_avg)

    for i in range(1,len(pts)):
                if pts[i-1]is None or pts[i]is None:
                    continue
                thickness = int(np.sqrt(64 / float(i + 1)) * 1)
                if thickness > 0:
                    cv.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
    cv.imshow('Contours', frame)

    for i in range(1,len(pts2)):
                if pts2[i-1]is None or pts2[i]is None:
                    continue
                thickness = int(np.sqrt(64 / float(i + 1)) * 1)
                if thickness > 0:
                    cv.line(frame, pts2[i - 1], pts2[i], (0, 255, 127), thickness)
    cv.imshow('Contours', frame)

    # =========================== 

    # makes video slower
    time.sleep(0.1)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

print("buy from CV app")