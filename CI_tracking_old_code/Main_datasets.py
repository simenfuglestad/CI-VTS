import cv2
import numpy
import os
import glob

datasets = "C:\\GIT_Projects\\MOT15\\train"
dataset = "PETS09-S2L1"

dir_images = datasets + "\\" + dataset + "\\img1\\"
file_label = datasets + "\\" + dataset + "\\gt\\gt.txt"

if not os.path.exists(file_label):
    print("file does not exist", file_label)
    quit()


data = numpy.genfromtxt(file_label, delimiter=',')
id_frame = 0
id_object = 0

for image in glob.glob(dir_images+"*.jpg"):
    frame = cv2.imread(image)

    mask = data[:, 0]==id_frame
    for d in data[mask, :]:
        cv2.rectangle(frame, (int(d[2]), int(d[3])), (int(d[2] + d[4]), int(d[3]+d[5])), (0, 255, 0), 2)
        xm = int(d[2]+d[4]/2)
        ym = int(d[3]+d[5]/2)

    cv2.imshow("frame",frame)

    key = cv2.waitKey(70)&0xFF
    if key==ord('q'):
        quit()
    id_frame+=1