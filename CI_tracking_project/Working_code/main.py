import cv2
import numpy as np
import os
import glob
import math
from KalmanFilter import KalmanFilter
from tracker.tracker import *


datasets = "C:\\GIT_Projects"
filename = "CI_Film.avi"
abs_path = datasets + "/" + filename

if not os.path.exists(datasets):
    print("Cant find path to ", datasets)
    quit()

if not os.path.exists(abs_path):
    print("Cant find path to ", filename)
    quit()

# largest tracking id
pop_num = 15

#Number of frames to reserve id
frames = 10

# Create a videoCapture object
cap = cv2.VideoCapture(abs_path)
detectionArray = []
tracker = init_tracker(pop_num,frames)
detector = cv2.createBackgroundSubtractorMOG2() # Removed history=100, varThreshold=10


i = 0
while True:
        ret, frame = cap.read()

        i += 1
        # Cropping frame. This can be removed
        #frame = frame[32:834, 845:1157]

        #Object detection
        mask = detector.apply(frame)
        #mask = cv2.adaptiveThreshold(mask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    #cv2.THRESH_BINARY, 11, 22)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        detectionArray.clear()
        for cnt in contours:
            # Calculate area of pixels then remove small elements.
            area = cv2.contourArea(cnt)
            #print(area)
            if area > 30 and area < 200:
                cv2.drawContours(frame, [cnt], -1, (0, 255, 0))
                x,y,w,h = cv2.boundingRect(cnt)
                detectionArray.append([x, y, w, h])

        points = []
        # Removing previous points
        points.clear()
        #Object tracking
        if i > 1:
            boxes_ids = tracker.update(detectionArray)
            for box_id in boxes_ids:
                x, y, w, h, id = box_id
                cv2.putText(frame, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                xm = int(x + w / 2)
                ym = int(y + h / 2)
                cv2.circle(frame, (xm, ym), 15, (0, 255, 0), 2)
                points.append([xm, ym, w, h, id, i])




        # Display the resulting tracking frame
        cv2.imshow('Tracking', frame)
        #cv2.imshow('mask', mask)

        # Slower the FPS
        cv2.waitKey(50)

        # Check for key strokes
        key = cv2.waitKey(50) & 0xff
        if key == 27:  # 'esc' key has been pressed, exit program.
            break



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


