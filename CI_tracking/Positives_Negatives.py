## Program to create negatives and positives from a videofile

import cv2

#Open videofile
capture = cv2.VideoCapture('Control_1 12-57-17.avi')
i = 0
while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == False:
        break
    if i%10 == 0:
        #neg = cv2.bitwise_not(frame)
        #rezise_neg = cv2.resize(neg,(300,200))
        # Går fra 85 til 780 i høyden og 905 til 1200 i bredden
        #crop_neg = neg[85:780,905:1200]

        crop_pos = frame[85:780, 905:1200]
        cv2.imwrite('Neg'+str(i)+'.jpg', crop_pos)
    i += 1

capture.realease()
cv2.destroyWindows()