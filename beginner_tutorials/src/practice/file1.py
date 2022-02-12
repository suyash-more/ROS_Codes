#!/usr/bin/env python

import os
import cv2 as cv
import numpy as np


path = os.path.join(os.path.dirname(__file__),'final.png')

img = cv.imread(path)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
gray = cv.cvtColor(hsv, cv.COLOR_BGR2GRAY)

cv.line(img, (0, 0), (300, 300), (0, 255, 0))

cv.imshow('Image BGR' ,img)
cv.imshow('Image HSV', hsv)
cv.imshow('Image Gray', gray)


cv.waitKey(0) 
  
# closing all open windows 
cv.destroyAllWindows() 