# managed to track CI using canny, blur and contours. It is still a bit nervous. Missing identities
import cv2
import numpy as np
import time
from matplotlib import pyplot as plt


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, offset=(1, 1))
    centers = []  # vector of object centroids in a frame

    # we only care about centroids with size of bug in this example
    blob_radius_min_thresh = 4
    blob_radius_max_thresh = 10
    # Find centroid for each valid contours
    for cnt in contours:
        try:
            # Calculate and draw circle
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            centeroid = (int(x), int(y))
            #print(centeroid)
            print(hierarchy)
            radius = int(radius)
            if (radius > blob_radius_min_thresh & radius < blob_radius_max_thresh):

                # If centeroid is bigger then new centeroid and c,y of new cnt is inside old x,y's radius
                cv2.circle(imgContour, centeroid, radius, (0, 255, 0), 2)
                b = np.array([[x], [y]])
                centers.append(np.round(b))
        except ZeroDivisionError:
            pass


def empty(a):
    pass
# Create a videoCapture object and read from input filter
capture = cv2.VideoCapture('CI_Film.avi')




if (capture.isOpened() == False):
    print("Error opening file")

while (capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:

        # Cropping video
        crop_frame = frame[32:834, 845:1157]
        imgContour = crop_frame.copy()
        imgGray = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)

        # Kernel for Dialation
        #kernel = np.ones((5, 5), np.uint8)

        # Testing Canny
        # Threshold1_1 = cv2.getTrackbarPos("Threshold1_1", "Adjust Canny")
        # Threshold1_2 = cv2.getTrackbarPos("Threshold1_2", "Adjust Canny")

        # adding blur to get less noise in the image
        blur = cv2.GaussianBlur(imgGray, (7, 7), 0)
        # filtering image to just show edges
        canny = cv2.Canny(blur, 27, 32)

        # Retain only edges within the threshold
        #ret, thresh = cv2.threshold(canny, 127, 255, 0)
        getContours(canny)
        #print("end frame")
        #time.sleep(5)


        # Tracking with canny and gaussian blur
        cv2.imshow('Contours', imgContour)


        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break
