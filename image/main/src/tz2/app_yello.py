#!/usr/bin/env python

# ..
import numpy as np
import cv2
# ..
# HSV color thresholds for YELLOW
THRESHOLD_LOW = (15, 210, 20)
THRESHOLD_HIGH = (35, 255, 255)


# Minimum required radius of enclosing circle of contour
MIN_RADIUS = 2

# 
# img_name  = 'messi5.jpg'
img_name  = 'biliard'
ball_collor  = 'yello'

# ..read
# Change Flag As 1 For Color Image
# or O for Gray Image So It image is 
# already gray
# https://stackoverflow.com/questions/30506126/open-cv-error-215-scn-3-scn-4-in-function-cvtcolor
img = cv2.imread('/data/%s_%s.jpg'%(img_name, ball_collor),1)
# ---------------

# # 01. Blur image to remove noise
img_filter = cv2.GaussianBlur(img.copy(), (3, 3), 0)


# 02. Convert image from BGR to HSV
img_filter = cv2.cvtColor(img_filter, cv2.COLOR_BGR2HSV)

# 03. Set pixels to white if in color range, others to black (binary bitmap)
img_binary = cv2.inRange(img_filter.copy(), THRESHOLD_LOW, THRESHOLD_HIGH)

# # 04. Dilate image to make white blobs larger
# img_binary = cv2.dilate(img_binary, None, iterations = 1)

# # 05. Find center of object using contours instead of blob detection. From:
# img_contours = img_binary.copy()
# contours = cv2.findContours(img_contours, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

# # 06. Find the largest contour and use it to compute the min enclosing circle
# center = None
# radius = 0
# if len(contours) > 0:
#     c = max(contours, key=cv2.contourArea)
#     ((x, y), radius) = cv2.minEnclosingCircle(c)
#     M = cv2.moments(c)
#     if M["m00"] > 0:
#         center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
#         if radius < MIN_RADIUS:
#             center = None

# # 07. Print out the location and size (radius) of the largest detected contour
# if center != None:
#     print(str(center) + " " + str(radius))

# # 09. Draw a green circle around the largest enclosed contour
# if center != None:
#     cv2.circle(img, center, int(round(radius)), (0, 255, 0))



# ---------------
# ..write
# cv2.imwrite('%s.png'%img_name, img)
# cv2.imwrite('%s.png'%img_name, img_filter)
cv2.imwrite('%s.png'%img_name, img_binary)