# Color detection through webcam 
# Use this to get hue, sat and val of the colour you need by adjusting the TrackBars.
# And use the value in the main program Virtual_marker.py

import cv2
import numpy as np


def empty():
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("val Max", "TrackBars", 255, 255, empty)


cap = cv2.VideoCapture(0)     # Reads vedio from webcaam
cap.set(3, 100)               # width as 3
cap.set(4, 100)               # height as 4
cap.set(10, 100)              # brightness as 10


while True:
    success, img = cap.read()

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)     #OUTPUT to import in Virtual_marker.py
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imageResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Original image', img)
    cv2.imshow('HSV image', imgHSV)
    cv2.imshow('masked image', mask)
    cv2.imshow('Result', imageResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # If q is pressed the vedio will end
        break

    cv2.waitKey(1)
