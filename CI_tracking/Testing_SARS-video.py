# managed to track CI using canny, blur and contours. It is still a bit nervous. Missing identities
import cv2
import numpy as np
from matplotlib import pyplot as plt

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # getting coordinates of contours
        area = cv2.contourArea(cnt)
        #print(area)
        #drawing contours
        if (area < 50):
            cv2.drawContours(imgContour,cnt,-1,(0,0,255),3)
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            #print (len(approx))
            object = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if (object > 4 & object < 10):
                objectType = "CI"
                cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(imgContour, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 1)
            else: print(object)






def empty(a):
    pass


# Create a videoCapture object and read from input filter
capture = cv2.VideoCapture('CI_Film.avi')

# Multipurpose trackbars for setup
#cv2.namedWindow("trackBars")
#cv2.resizeWindow("trackBars", 640, 240)


# Slider for canny
cv2.namedWindow("Adjust Canny")
cv2.resizeWindow("Adjust Canny", 600, 140)
cv2.createTrackbar("Threshold1_1", "Adjust Canny", 0, 1000,empty)
cv2.createTrackbar("Threshold1_2", "Adjust Canny", 0, 1000,empty)
cv2.createTrackbar("Dialation", "Adjust Canny", 0, 1000,empty)
cv2.createTrackbar("erosion", "Adjust Canny", 0, 1000,empty)

# sliders for filtering
#cv2.namedWindow("Adjust mask")
#cv2.resizeWindow("Adjust mask", 600, 140)
#cv2.createTrackbar("HSV1", "Adjust mask", 0, 255,empty)
#cv2.createTrackbar("HSV2", "Adjust mask", 0, 255,empty)
#cv2.createTrackbar("HSV3", "Adjust mask", 0, 255,empty)


if (capture.isOpened() == False):
    print("Error opening file")

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:

        # Sliders to crop image
        #MinX = cv2.getTrackbarPos("MinX", "trackBars")
        #MaxX = cv2.getTrackbarPos("MaxX", "trackBars")
        #MinY = cv2.getTrackbarPos("MinY", "trackBars")
        #MaxY = cv2.getTrackbarPos("MaxY", "trackBars")
        #AdjThresh = cv2.getTrackbarPos("thresh", "trackBars")

        # Cropping video
        crop_frame = frame[32:834, 845:1157]
        imgContour = crop_frame.copy()
        imgGray = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)

        # Kernel for Dialation
        kernel = np.ones((5, 5), np.uint8)
        # Testing Canny
        Threshold1_1 = cv2.getTrackbarPos("Threshold1_1", "Adjust Canny")
        Threshold1_2 = cv2.getTrackbarPos("Threshold1_2", "Adjust Canny")
        dialation = cv2.getTrackbarPos("Dialation", "Adjust Canny")
        erosion = cv2.getTrackbarPos("erosion", "Adjust Canny")
        # adding blur to get less noise in the image
        blur = cv2.GaussianBlur(imgGray, (7, 7),0)
        # filtering image to just show edges
        canny = cv2.Canny(blur, Threshold1_1, Threshold1_2)
        # making edges thicker
        cannyDialation = cv2.dilate(canny,kernel,iterations = dialation)
        #eroding image
        erodedimg = cv2.erode(cannyDialation, kernel, iterations=erosion)
        getContours(canny)


        #Filtering image
        #HSV1 = cv2.getTrackbarPos('HSV1', 'Adjust mask')
        #HSV2 = cv2.getTrackbarPos('HSV2', 'Adjust mask')
        #HSV3 = cv2.getTrackbarPos('HSV3', 'Adjust mask')
        #Trying to filter original film
        #hsv = cv2.cvtColor(crop_frame,cv2.COLOR_BGR2HSV)

        # Array for red
        #lower_red = np.array([HSV1,HSV2,HSV3])
        #upper_red = np.array([255,255,255])

        #mask = cv2.inRange(hsv, lower_red, upper_red)
        #result = cv2.bitwise_and(crop_frame, crop_frame , mask = mask)


        # Filtering image
        #cv2.imshow('frame',hsv)
        #cv2.imshow('mask', mask)
        #cv2.imshow('result', result)

        # Tracking with canny and gaussian blur
        cv2.imshow('Contours', imgContour)
        cv2.imshow('Canny', canny)
        cv2.imshow('blur', blur)
        cv2.imshow('Cropped image', crop_frame)
        cv2.imshow('dialated', cannyDialation)
        cv2.imshow('erodedimg', erodedimg)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

