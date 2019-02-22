# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:51:17 2018

@author: hongb
"""

import cv2
import numpy as np
image = cv2.imread("elephant.jpg")
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyWindow("Image")