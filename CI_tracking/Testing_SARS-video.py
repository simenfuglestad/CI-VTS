# Import librarys
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

#cv2.namedWindow("trackBars")
#cv2.resizeWindow("trackBars", 640, 240)

# Some trackbars
#cv2.createTrackbar("MinX", "trackBars", 40, 1300,empty)
#cv2.createTrackbar("MaxX", "trackBars", 100, 1300,empty)
#cv2.createTrackbar("MinY", "trackBars", 40, 1300,empty)
#cv2.createTrackbar("MaxY", "trackBars", 200, 1300,empty)
#cv2.createTrackbar("thresh", "trackBars", 0, 255,empty)
#cv2.createTrackbar("Gamma", "trackBars", 0, 255,empty)

# Adjusting Colors in HSV
#cv2.createTrackbar("Hue Min", "trackBars", 0, 179,empty)
#cv2.createTrackbar("Hue Max", "trackBars", 179, 179,empty)
#cv2.createTrackbar("Sat Min", "trackBars", 0, 255,empty)
#cv2.createTrackbar("Sat Max", "trackBars", 255, 255,empty)
#v2.createTrackbar("Val Min", "trackBars", 0, 255,empty)
#v2.createTrackbar("Val Max", "trackBars", 255, 255,empty)

# Gausian blur and canny
#cv2.namedWindow("Gausian and canny")
#cv2.resizeWindow("Gausian and canny", 640, 240)
#cv2.createTrackbar("Can value from", "Gausian and canny", 0, 1000,empty)
#cv2.createTrackbar("Can value to", "Gausian and canny", 0, 1000,empty)


if (capture.isOpened() == False):
    print("Error opening file")

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        #MinX = cv2.getTrackbarPos("MinX", "trackBars")
        #MaxX = cv2.getTrackbarPos("MaxX", "trackBars")
        #MinY = cv2.getTrackbarPos("MinY", "trackBars")
        #MaxY = cv2.getTrackbarPos("MaxY", "trackBars")
        #AdjThresh = cv2.getTrackbarPos("thresh", "trackBars")

        #Adjusting colors in HSV
        #h_min = cv2.getTrackbarPos("Hue Min", "trackBars")
        #h_max = cv2.getTrackbarPos("Hue Max", "trackBars")
        #s_min = cv2.getTrackbarPos("Sat Min", "trackBars")
        #s_max = cv2.getTrackbarPos("Sat Max", "trackBars")
        #v_min = cv2.getTrackbarPos("Val Min", "trackBars")
        #v_max = cv2.getTrackbarPos("Val Max", "trackBars")
        #print(h_min,h_max,s_min,s_max,v_min,v_max)

        # Cropping video
        crop_frame = frame[32:834, 845:1157]
        imgContour = crop_frame.copy()
        imgGray = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)

        # Testing colors
        #imgHSV = cv2.cvtColor(crop_frame,cv2.COLOR_RGB2HSV)
        #lower = np.array([h_min,s_min,v_min])
        #upper = np.array([h_max,s_max,v_max])
        #mask = cv2.inRange(imgHSV,lower,upper)

        ## Testing thresh
        #gray = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)
        #(thresh, blackAndWhiteImage) = cv2.threshold(gray,196,255,cv2.THRESH_BINARY)

        # distributed histogram
        #equ = cv2.equalizeHist(blackAndWhiteImage)
        #plt.imshow(equ)

        # Testing HoughLines
        #gray = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)

        # Testing Canny
        #cannyValFrom = cv2.getTrackbarPos("Can value from", "Gausian and canny")
        #cannyValTo = cv2.getTrackbarPos("Can value to", "Gausian and canny")
        blur = cv2.GaussianBlur(imgGray, (13, 13),1)
        canny = cv2.Canny(blur, 27, 41)
        getContours(canny)




        cv2.imshow('Contours', imgContour)
        cv2.imshow('Canny', canny)
        cv2.imshow('blur', blur)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

