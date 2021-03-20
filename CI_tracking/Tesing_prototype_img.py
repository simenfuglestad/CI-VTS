import cv2
import numpy as np
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # getting coordinates of contours
        area = cv2.contourArea(cnt)
        print(area)
        #drawing contours
        cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)

def empty(a):
    pass


#cv2.createTrackbar("MinX", "trackBars", 40, 1300,empty)
#cv2.createTrackbar("MaxX", "trackBars", 100, 1300,empty)
#cv2.createTrackbar("MinY", "trackBars", 40, 1300,empty)
#cv2.createTrackbar("MaxY", "trackBars", 100, 1300,empty)

# Adjusting Colors in HSV
cv2.namedWindow("COLORS HSV")
cv2.resizeWindow("COLORS HSV", 640, 240)
cv2.createTrackbar("Hue Min", "COLORS HSV", 0, 179,empty)
cv2.createTrackbar("Hue Max", "COLORS HSV", 179, 179,empty)
cv2.createTrackbar("Sat Min", "COLORS HSV", 0, 255,empty)
cv2.createTrackbar("Sat Max", "COLORS HSV", 255, 255,empty)
cv2.createTrackbar("Val Min", "COLORS HSV", 0, 255,empty)
cv2.createTrackbar("Val Max", "COLORS HSV", 255, 255,empty)

# Gausian blur and canny
cv2.namedWindow("Gausian and canny")
cv2.resizeWindow("Gausian and canny", 640, 240)
cv2.createTrackbar("Can value from", "Gausian and canny", 0, 1000,empty)
cv2.createTrackbar("Can value to", "Gausian and canny", 0, 1000,empty)


while True:

    img = cv2.imread("ImageSNAP_3.bmp")


    # Resizing image
    imgRes = cv2.resize(img,(800, 700))
    print(imgRes.shape)

    # Cropping image
    imgCrop = imgRes[0:606,310:474]
    imgContour = imgCrop.copy()
    imgGray = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY)
    #MinX = cv2.getTrackbarPos("MinX", "trackBars")
    #MaxX = cv2.getTrackbarPos("MaxX", "trackBars")
    #MinY = cv2.getTrackbarPos("MinY", "trackBars")
    #MaxY = cv2.getTrackbarPos("MaxY", "trackBars")

    # Testing colors
    h_min = cv2.getTrackbarPos("Hue Min", "COLORS HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "COLORS HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "COLORS HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "COLORS HSV")
    v_min = cv2.getTrackbarPos("Val Min", "COLORS HSV")
    v_max = cv2.getTrackbarPos("Val Max", "COLORS HSV")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    imgHSV = cv2.cvtColor(imgCrop,cv2.COLOR_RGB2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    # Testing Canny
    cannyValFrom = cv2.getTrackbarPos("Can value from", "Gausian and canny")
    cannyValTo = cv2.getTrackbarPos("Can value to", "Gausian and canny")
    blur = cv2.GaussianBlur(imgGray,(5,5),0)
    canny = cv2.Canny(blur, cannyValFrom, cannyValTo)
    getContours(canny)

    # Testing thresh
    #gray = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY)
    #(thresh, blackAndWhiteImage) = cv2.threshold(gray,196,255,cv2.THRESH_BINARY)

    #cv2.imshow("image", img)
    #cv2.imshow("imageRes", imgRes)

    cv2.imshow("imgMask", mask)
    cv2.imshow("imgCrop", imgCrop)
    cv2.imshow("imgCanny", canny)
    cv2.imshow("Contours",imgContour)

    cv2.waitKey(1)

