# Virtual Marker

import cv2
import numpy as np

framewidth = 3000
frameheight = 2000
cap = cv2.VideoCapture(0)   # Reads vedio from webcaam
cap.set(3, framewidth)      # width as 3
cap.set(4, frameheight)     # height as 4
cap.set(10, 0)            # brightness as 10

# Using colour_detection.py, get the required colour to me marked and note the hue sat and val and upload in myColors. 

myColors = [[94, 201, 133, 122, 255, 255],
            [166, 159, 100, 179, 255, 255],
            [116, 72, 165, 166, 255, 255],
            [78, 143, 102, 89, 255, 255],
            [90, 168, 181, 100, 255, 255],
            [20, 44, 255, 37, 255, 255]]

# colors_name = ['Blue', 'Red', 'Violet', 'Light Green', 'Green', 'Yellow' ]

MyColorValues = [[153, 0, 0], [0, 0, 255], [128, 0, 64], [26, 255, 26], [0, 255, 0], [26, 255, 255]] # Color to be printed

mypoints = []  # [x, y, colorId]


def findColor(img, myColors, MyColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # c = -1
    count = 0
    newpoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, MyColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newpoints.append([x, y, count])
        count += 1
        # c+=1
        # cv2.imshow(colors_name[c], mask)
    return newpoints


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)  # -1 to print all shape
            peri = cv2.arcLength(cnt, True)
            aprox = cv2.approxPolyDP(cnt, 0.02*peri, True)  # True because its a closed image
            x, y, w, h = cv2.boundingRect(aprox)
    return x + w // 2, y


def draw(mypoints, MyColorValues):
    for point in mypoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, MyColorValues[point[2]], cv2.FILLED)  # (image, (point 1, point 2), radius, color, thickness)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newpoints = findColor(img, myColors, MyColorValues)
    if len(newpoints) != 0:
        for newp in newpoints:
            mypoints.append(newp)
    if len(mypoints) != 0:
        draw(mypoints, MyColorValues)
    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # If q is pressed the video will end
        break
