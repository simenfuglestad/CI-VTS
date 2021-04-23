import cv2
import numpy as np
from numpy import genfromtxt
from KalmanFilter import KalmanFilter
import math
import os
import glob

datasets = "C:\\GIT_Projects\\MOT15\\train"
dataset = "PETS09-S2L1"



dir_images=datasets+"/"+dataset+"/img1/"
file_label= datasets + "/" + dataset + "/gt/gt.txt"

if not os.path.exists(dir_images):
    print("Funkje serru", dir_images)
    quit()

if not os.path.exists(file_label):
    print("Funkje serru", file_label)
    quit()

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

data=genfromtxt(file_label, delimiter=',')
id_frame=0
id_object=0

start=0
for image in glob.glob(dir_images+"*.jpg"):
    frame=cv2.imread(image)

    # Prediction of all objects + display
    for id_obj in range(len(objects_points)):
        print(objects_points)
        state=objects_KF[id_obj].predict()
        state=np.array(state, dtype=np.uint32)
        print(state.itemsize)
        objects_points[id_obj]=np.array([state[0], state[1], state[4], state[5]])
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
        if objects_id[id_obj]==0:
            cv2.arrowedLine(frame,
                            (int(state[0]), int(state[1] - state[5] / 2 - 80)),
                            (int(state[0]), int(state[1] - state[5] / 2 - 30)),
                            color=(0, 0, 255),
                            thickness=5,
                            tipLength=0.2)

    # Retrieving the objects from frame
    mask=data[:, 0]==id_frame

    # Detector data display (rectangle)
    points=[]
    for d in data[mask, :]:
        #if np.random.randint(2):
        if rectangle:
            cv2.rectangle(frame, (int(d[2]), int(d[3])), (int(d[2]+d[4]), int(d[3]+d[5])), (0, 255, 0), 2)
        xm=int(d[2]+d[4]/2)
        ym=int(d[3]+d[5]/2)
        cv2.circle(frame, (xm, ym), 2, (0, 255, 0), 2)
        points.append([xm, ym, int(d[4]), int(d[5])])

    #calculating distance
    new_objects=np.ones((len(points)))
    tab_distances=[]
    if len(objects_points):
        for point_id in range(len(points)):
            distances=distance(points[point_id], objects_points)
            tab_distances.append(distances)

        tab_distances=np.array(tab_distances)
        sorted_distances=np.sort(tab_distances, axis=None)

        for d in sorted_distances:
            if d>distance_mini:
                break
            id1, id2=np.where(tab_distances==d)
            if not len(id1) or not len(id2):
                continue
            tab_distances[id1, :]=distance_mini+1
            tab_distances[:, id2]=distance_mini+1
            objects_KF[id2[0]].update(np.expand_dims(points[id1[0]], axis=-1))
            new_objects[id1]=0

    # Creation of the Kalman filter for new objects
    for point_id in range(len(points)):
        if new_objects[point_id]:
            print("NEW", points[point_id])
            objects_points.append(points[point_id])
            objects_KF.append(KalmanFilter(0.5, [points[point_id][0], points[point_id][1]], [points[point_id][2], points[point_id][3]]))
            objects_id.append(id_object)
            objects_history.append([])
            id_object+=1

    # Cleaning ...
    tab_id=[]
    for id_point in range(len(objects_points)):
        if int(objects_points[id_point][0])<-100 or \
        int(objects_points[id_point][1])<-100 or \
            objects_points[id_point][0]>frame.shape[1]+100 or \
            objects_points[id_point][1]>frame.shape[0]+100:
            print("SUPPRESSION", objects_points[id_point])
            tab_id.append(id_point)

    for index in sorted(tab_id, reverse=True):
        del objects_points[index]
        del objects_KF[index]
        del objects_id[index]
        del objects_history[index]

    cv2.rectangle(frame, (0, 0), (frame.shape[1], 30), (100, 100, 100), cv2.FILLED)
    message="Frame: {:03d}  Nbr person: {:d}  nbr filter: {:d}   [r]Rectangle: {:3}  [t]Trace: {:3}".format(id_frame,
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

    cv2.imshow("frame", frame)
    key=cv2.waitKey(70)&0xFF
    if key==ord('r'):
        rectangle=not rectangle
    if key==ord('t'):
        trace=not trace
    if key==ord('q'):
        quit()
    id_frame+=1