#!/usr/bin/env python

# ..
import numpy as np
import cv2

IMG_NAME  = 'naturmort2'

# .. read image
img = cv2.imread('/data/%s.jpg'%IMG_NAME,1)
template = cv2.imread('/data/%s_tpl.jpg'%IMG_NAME,1)
w, h  = template.shape[:-1]
# ========================

# 1. match template
res = cv2.matchTemplate(img.copy(), template, cv2.TM_CCOEFF)

# 2. calculate rectangle coordinates
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
print(top_left, bottom_right)

# 3. to paint blue rectangle
cv2.rectangle(img, top_left, bottom_right, 255, 2)



# ========================
# ..write
cv2.imwrite('%s.png'%IMG_NAME, img)