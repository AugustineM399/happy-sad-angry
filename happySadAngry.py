# py C:\Users\Owner\PythonCoding\happySadAngry\happySadAngry.py

# importations
import pathlib
# 2.
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
# 4.
import requests
# 5.
import os
# 6.
import uuid
import time

# load model
parentDir = str(pathlib.Path(__file__).parent)
model = torch.hub.load('ultralytics/yolov5', 'custom', path=parentDir+"/best.pt", force_reload=True)

# testing
pathlib.Path(parentDir+"/test").mkdir(parents=True, exist_ok=True)
if not os.path.exists(parentDir+"/test/num.txt"):
    f = open(parentDir+"/test/num.txt", "w")
    f.write("0")
    f.close()
repeat = "R" == input("Input R to enter single-image and results saving mode, or ENTER to skip straight to live camera detections.")
while repeat:
    f = open(parentDir+"/test/num.txt", "r")
    num = int(f.read())
    f.close()

    f = open(parentDir+"/test/num.txt", "w")
    f.write(str(num + 1))
    f.close()

    cam = cv2.VideoCapture(0)
    s, img = cam.read() # take a pic
    if s:
        filename = parentDir+"/test/" + str(num) + ".jpg"
        cv2.imwrite(filename,img) # save image
    time.sleep(3)
    results = model(filename)
    print(results)
    rendered_image = np.squeeze(results.render())
    print(rendered_image.shape)
    plt.imshow(rendered_image)

    # Display the image
    plt.savefig(parentDir+"/test/" + str(num) + "result.jpg")
    plt.show()

    print(f"Image and results saved to {num}.jpg and {num}result.jpg")
    repeat = "R" == input("Hit ENTER to finish, or input R to repeat.")

cap = cv2.VideoCapture(0)
print("Hit ESCAPE to exit the video feed.")
while cap.isOpened():
    ret, frame = cap.read()

    # Make detections
    results = model(frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))

    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()