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

tracker = EuclideanDistTracker()
distance_mini=500
rectangle=0
trace=0

objects_points=[]
objects_id=[]
objects_KF=[]
objects_history=[]

def distance(point, liste_points):
    distances=[]
    for p in liste_points:
        distances.append(np.sum(np.power(p-np.expand_dims(point, axis=-1), 2)))
    return distances
def trace_history(tab_points, length, color=(0, 255, 255)):
    history=np.array(tab_points)
    nbr_point=len(history)
    length=min(nbr_point, length)
    for i in range(nbr_point-1, nbr_point - length, -1):
        cv2.line(frame,
                 (int(history[i - 1, 0]), int(history[i - 1, 1])),
                 (int(history[i, 0]), int(history[i, 1])),
                 color,
                 2)

detector = cv2.createBackgroundSubtractorMOG2() # Removed history=100, varThreshold=10
id_frame=0
id_objet=0
start=0
#tracker = Tracker()
detectionArray = []
z = -1
i = 0
while True:
        ret, frame = cap.read()

        i += 1

        #Object detection
        mask = detector.apply(frame)
        #can = cv2.Canny(mask, 27, 27)
        #_, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            # Calculate area of pixels then remove small elements.
            area = cv2.contourArea(cnt)
            if area > 30:
                #cv2.drawContours(frame, [cnt], -1, (0, 255, 0))
                x,y,w,h = cv2.boundingRect(cnt)
                detectionArray.append([x, y, w, h])

        print(detectionArray)
        points = []
        #Object tracking
        boxes_ids = tracker.update(detectionArray)
        #print(boxes_ids)
        for box_id in boxes_ids:
            x, y, w, h, id = box_id
            cv2.putText(frame, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            if rectangle:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            xm = int(x + w / 2)
            ym = int(y + h / 2)
            cv2.circle(frame, (xm, ym), 2, (0, 255, 0), 2)
            points.append([xm, ym, w, h])



        # Prediction of all objects + display
        for id_obj in range(len(objects_points)):

            # sett inn x,y,w,h
            state = objects_KF[id_obj].predict()
            state = np.array([i, id, x, y, w, h, 1, x, y, z])
            #print(state.itemsize)
            objects_points[id_obj] = np.array([state[0], state[1], state[4], state[5]])
            objects_history[id_obj].append([state[0], state[1]])
            cv2.circle(frame, (int(state[0]), int(state[1])), 5, (0, 0, 255), 2)
            if rectangle:
                cv2.rectangle(frame,
                              (int(state[0] - state[4] / 2), int(state[1] - state[5] / 2)),
                              (int(state[0] + state[4] / 2), int(state[1] + state[5] / 2)),
                              (0, 0, 255),
                              2)
            cv2.arrowedLine(frame,
                            (int(state[0]), int(state[1])),
                            (int(state[0] + 3 * state[2]), int(state[1] + 3 * state[3])),
                            color=(0, 0, 255),
                            thickness=2,
                            tipLength=0.2)
            cv2.putText(frame,
                        "ID{:d}".format(objects_id[id_obj]),
                        (int(state[0] - state[4] / 2), int(state[1] - state[5] / 2)),
                        cv2.FONT_HERSHEY_PLAIN,
                        1.5,
                        (255, 0, 0),
                        2)

            if trace:
                trace_history(objects_history[id_obj], 42)

            # Allows you to follow the ID 0 with an arrow
            if objects_id[id_obj] == 0:
                cv2.arrowedLine(frame,
                                (int(state[0]), int(state[1] - state[5] / 2 - 80)),
                                (int(state[0]), int(state[1] - state[5] / 2 - 30)),
                                color=(0, 0, 255),
                                thickness=5,
                                tipLength=0.2)

        # Retrieving the objects from frame
        #mask = data[:, 0] == id_frame

          # Detector data display (rectangle)




        # calculating distance
        new_objects = np.ones((len(points)))
        tab_distances = []
        if len(objects_points):
            for point_id in range(len(points)):
                distances = distance(points[point_id], objects_points)
                tab_distances.append(distances)

            tab_distances = np.array(tab_distances)
            sorted_distances = np.sort(tab_distances, axis=None)

            for d in sorted_distances:
                if d > distance_mini:
                    break
                id1, id2 = np.where(tab_distances == d)
                if not len(id1) or not len(id2):
                    continue
                tab_distances[id1, :] = distance_mini + 1
                tab_distances[:, id2] = distance_mini + 1
                objects_KF[id2[0]].update(np.expand_dims(points[id1[0]], axis=-1))
                new_objects[id1] = 0

        # Creation of the Kalman filter for new objects
        for point_id in range(len(points)):
            if new_objects[point_id]:
                #print("NEW", points[point_id])
                objects_points.append(points[point_id])
                objects_KF.append(KalmanFilter(0.5, [points[point_id][0], points[point_id][1]],
                                               [points[point_id][2], points[point_id][3]]))
                objects_id.append(id_objet)
                objects_history.append([])
                id_objet += 1

        # Cleaning ...
        tab_id = []
        for id_point in range(len(objects_points)):
            if int(objects_points[id_point][0]) < -100 or \
                    int(objects_points[id_point][1]) < -100 or \
                    objects_points[id_point][0] > frame.shape[1] + 100 or \
                    objects_points[id_point][1] > frame.shape[0] + 100:
                print("SUPPRESSION", objects_points[id_point])
                tab_id.append(id_point)

        for index in sorted(tab_id, reverse=True):
            del objects_points[index]
            del objects_KF[index]
            del objects_id[index]
            del objects_history[index]

        cv2.rectangle(frame, (0, 0), (frame.shape[1], 30), (100, 100, 100), cv2.FILLED)
        message = "Frame: {:03d}  Nbr object: {:d}  nbr filter: {:d}   [r]Rectangle: {:3}  [t]Trace: {:3}".format(
            i,
            len(points),
            len(objects_points),
            "ON" if rectangle else "OFF",
            "ON" if trace else "OFF")
        cv2.putText(frame,
                    message,
                    (20, 20),
                    cv2.FONT_HERSHEY_PLAIN,
                    1,
                    (255, 255, 255),
                    1)













        # Display the resulting tracking frame
        cv2.imshow('Tracking', frame)

        # Cleaning up the dodlidoos
        detectionArray.clear()

        # Display the original frame
        #cv2.imshow('Original', orig_frame)

        # Slower the FPS
        cv2.waitKey(50)

        # Check for key strokes
        key = cv2.waitKey(0) & 0xff
        if key == 27:  # 'esc' key has been pressed, exit program.
            break
        if key == ord('r'):
            rectangle = not rectangle
        if key == ord('t'):
            trace = not trace
        if key == 112:  # 'p' has been pressed. this will pause/resume the code.
            pause = not pause
            if (pause is True):
                print("Code is paused. Press 'p' to resume..")
                while (pause is True):
                    # stay in this loop until
                    key = cv2.waitKey(30) & 0xff
                    if key == 112:
                        pause = False
                        print("Resume code..!!")
                        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


