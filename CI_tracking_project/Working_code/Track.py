import cv2
import numpy as np
import os
import glob
import math
from KalmanFilter import KalmanFilter
from tracker.tracker import *

# Combination of Tracking_Multiple and Partly_success_id Track.py
class track_init:
    def __init__(self):
        self.detectionArray = []
        self.tracker = EuclideanDistTracker()
        self.detector = cv2.createBackgroundSubtractorMOG2() # Removed history=100, varThreshold=10
        self.i = 0
    def track(self, frame):

        # Create a videoCapture object and read from input filter
        self.i += 1

        #Object detection
        mask = self.detector.apply(frame)
        #mask = cv2.adaptiveThreshold(mask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    #cv2.THRESH_BINARY, 11, 22)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        self.detectionArray.clear()
        for cnt in contours:
            # Calculate area of pixels then remove small elements.
            area = cv2.contourArea(cnt)
            #print(area)
            if area > 30 and area < 200:
                cv2.drawContours(frame, [cnt], -1, (0, 255, 0))
                x,y,w,h = cv2.boundingRect(cnt)
                self.detectionArray.append([x, y, w, h])
                #print(detectionArray)
                #cv2.minEnclosingCircle(cnt)

        points = []
        # Removing previous points
        points.clear()
        #Object tracking
        if self.i > 5:
            boxes_ids = self.tracker.update(self.detectionArray)
            #print(boxes_ids)
            for box_id in boxes_ids:
                x, y, w, h, id = box_id
                cv2.putText(frame, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                xm = int(x + w / 2)
                ym = int(y + h / 2)
                #cv2.circle(frame, (xm, ym), 10, (0, 255, 0), 2)
                points.append([xm, ym, w, h, id, self.i])


        cv2.rectangle(frame, (0, 0), (frame.shape[1], 30), (100, 100, 100), cv2.FILLED)
        message = "Test"
        cv2.putText(frame,
                    message,
                    (20, 20),
                    cv2.FONT_HERSHEY_PLAIN,
                    1,
                    (255, 255, 255),
                    1)

        return frame, boxes_ids




