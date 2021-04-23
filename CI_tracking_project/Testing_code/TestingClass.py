from Testing_code.Track import *

# Combination of Tracking_Multiple and Partly_success_id Track.py

datasets = "C:\\GIT_Projects"
filename = "CI_Film.avi"
abs_path = datasets + "/" + filename

if not os.path.exists(datasets):
    print("Funkje serru: finner ikke veien til mappen", datasets)
    quit()

if not os.path.exists(abs_path):
    print("Funkje serru: finner ikke den såkalte filen", filename)
    quit()

track = track_init()
data = {}
# Create a videoCapture object and read from input filter
cap = cv2.VideoCapture(abs_path)
while True:
        ret, frame = cap.read()

        data, frame = track.tracker(frame)

        # Display the resulting tracking frame
        cv2.imshow('Tracking', frame)
        # cv2.imshow('mask', mask)

        # Slower the FPS
        cv2.waitKey(50)

        # Check for key strokes
        key = cv2.waitKey(50) & 0xff
        if key == 27:  # 'esc' key has been pressed, exit program.
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()