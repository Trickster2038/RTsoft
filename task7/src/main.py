import cv2 as cv
import numpy as np
import time
from collections import deque
import paho.mqtt.client as mqtt
import json

def running_mean(x, N):
    """ 
    x == an array of data
    N == number of samples per average 
    """
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

def pts_avg(pts, N): 
    """ 
    pts == a deque of points
    N == number of samples per average 
    """
    pts_list = list(pts)
    list_x = []
    list_y = []

    for elem in pts_list:
        list_x = np.append(list_x, list(elem)[0])
        list_y = np.append(list_y, list(elem)[1])

    x_avg = running_mean(list_x, min([len(list_x),N]))
    y_avg = running_mean(list_y, min([len(list_y),N]))

    pts2 = deque(maxlen=124)

    for i in range(0,len(x_avg)):
        pts2.append((int(x_avg[i]), int(y_avg[i])))

    return pts2

def draw_track(pts, k, color):
    """ 
    pts == a deque of points
    k == thickness coefficient
    color == (r,g,b) color
    """
    for i in range(1,len(pts)):
            if pts[i-1]is None or pts[i]is None:
                continue
            thickness = int(np.sqrt(64 / float(i + 1)) * k - k)
            if thickness > 0:
                cv.line(frame, pts[i - 1], pts[i], color, thickness)
    cv.imshow('Contours', frame)

def resize_img(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    return resized

def get_contours(img, N):
    """ 
    img == image
    N == number of contours to get
    """
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edged = cv.Canny(gray, 30, 200)
    contours, hierarchy = cv.findContours(edged, \
    cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    return contours[0:N]



if __name__ == "__main__":

    print("hello from CV app")
    pts = deque(maxlen=124)
    cap = cv.VideoCapture('test2.mp4')
    i = 0

    client = mqtt.Client("cvSubscriber1")
    status = client.connect("localhost")
    if status == 0:
        print("MQQT connected")
    else:
        print("MQQT is down")

    while cap.isOpened():
        # print("CV-loop")
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # main part ================= 

        frame = resize_img(frame, 60)   
        contours2 = get_contours(frame, 7)

        # cv.drawContours(frame, contours2, -1, (0, 255, 0), 1)

        
        for cnt in contours2:
            x,y,w,h = cv.boundingRect(cnt)
            if frame.shape[1]/w < 30 and frame.shape[0]/h < 30: # check that frame is huge enough
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,200),2) # draw rectangles
                center=(int(x+w/2),int(y+h/2)) # count center
                pts.appendleft(center) # add center to track 

        avg_pts = pts_avg(pts, 10)
        # draw_track(pts, 1, (255,0, 0))
        draw_track(avg_pts, 2, (0,255,0))

        i += 1
        if i % 1 == 0:
            # print(avg_pts[0])
            x = list(pts[0])[0]
            y = list(pts[0])[1]
            x_avg = list(avg_pts[0])[0]
            y_avg = list(avg_pts[0])[1]
            msg = json.dumps({"x":x, "y":y, "x corrected":x_avg, "y corrected": y_avg})
            # client.publish("cv/track", str(avg_pts[0]))
            client.publish("cvtrack", msg)
            # print("MQTT send: ", msg)

        # =========================== 

        # makes video slower
        time.sleep(0.1)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
    print("good bye from CV app")