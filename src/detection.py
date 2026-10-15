import cv2
import numpy as np

# Color range for the golf ball used
LOWER = np.array([163, 100, 100])
UPPER = np.array([179, 255, 255])


def detect_ball(frame):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, LOWER, UPPER)

    contours,_ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return None

    ball = max(contours, key=cv2.contourArea)
    (x, y), radius = cv2.minEnclosingCircle(ball)


    return x, y, radius



def convert_pos(x_p, y_p, x0, y0, radius_p):

    diameter_p = 2*radius_p
    diameter_m = 42.67

    scale = diameter_p/diameter_m

    x = (x_p-x0)/scale
    y = (y0 - y_p)/scale

    return x, y


def detect_movement(positions, min_dist=5):

    for index, x, y, in positions:
        dist = np.sqrt(x**2 + y**2)

        if dist > min_dist :
            return index

    return None





