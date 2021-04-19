import cv2
import numpy as np
import os
import glob
import math
from KalmanFilter import KalmanFilter
from tracker.tracker import *

# Combination of Tracking_Multiple and Partly_success_id Main.py

datasets = "C:\\GIT_Projects"
filename = "CI_Film.avi"
abs_path = datasets + "/" + filename

if not os.path.exists(datasets):
    print("Funkje serru: finner ikke veien til mappen", datasets)
    quit()

if not os.path.exists(abs_path):
    print("Funkje serru: finner ikke den såkalte filen", filename)
    quit()

# Create a videoCapture object and read from input filter
cap = cv2.VideoCapture(abs_path)


detectionArray = []
tracker = EuclideanDistTracker()

detector = cv2.createBackgroundSubtractorMOG2() # Removed history=100, varThreshold=10

i = 0
while True:
        ret, frame = cap.read()

        i += 1


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
                #cv2.minEnclosingCircle(cnt)

        points = []
        # Removing previous points
        points.clear()
        #Object tracking
        if i > 5:
            boxes_ids = tracker.update(detectionArray)
            #print(boxes_ids)
            for box_id in boxes_ids:
                x, y, w, h, id = box_id
                cv2.putText(frame, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                xm = int(x + w / 2)
                ym = int(y + h / 2)
                #cv2.circle(frame, (xm, ym), 10, (0, 255, 0), 2)
                points.append([xm, ym, w, h, id, i])


        cv2.rectangle(frame, (0, 0), (frame.shape[1], 30), (100, 100, 100), cv2.FILLED)
        message = "Test"
        cv2.putText(frame,
                    message,
                    (20, 20),
                    cv2.FONT_HERSHEY_PLAIN,
                    1,
                    (255, 255, 255),
                    1)


        # Display the resulting tracking frame
        cv2.imshow('Tracking', frame)
        #v2.imshow('mask', mask)

        # Slower the FPS
        cv2.waitKey(50)

        # Check for key strokes
        key = cv2.waitKey(50) & 0xff
        if key == 27:  # 'esc' key has been pressed, exit program.
            break



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


