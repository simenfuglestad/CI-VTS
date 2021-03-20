import cv2

# Source data : Video File
Video_file = 'Control_1 12-57-17.avi'

# Read the source video file
vid_file = cv2.VideoCapture(Video_file)

# pre trained classifiers
larvae_classifier = 'Ciona_Intestinalis_crop.xml'


# Classified Trackers
larvae_tracker = cv2.CascadeClassifier(larvae_classifier)



while True:
    # start reading video file
    (read_successful, frame) = vid_file.read()

    if read_successful:
        #Show only inside of cuvette
        crop_frame = frame[85:780, 905:1200]
        #convert to grey scale image
        gray_frame = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect larvae
    larvae = larvae_tracker.detectMultiScale(gray_frame, 1.1, 9)



    # Draw rectangle around the larvae
    for (x, y, w, h) in larvae:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, 'Larvae', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        #cv2.rectangle(gray_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


    # display the image
    cv2.imshow('Detect Objects in cuvette',frame)

    # capture key
    key = cv2.waitKey(1)

    # Stop if Esc is pressed
    if key == 27:
        break

# Release video capture object
vid_file.release()

print("Done")
