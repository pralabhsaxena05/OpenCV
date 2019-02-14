import numpy as np
import cv2 as cv
img = cv.imread('pralabh.jpeg')
matrix = (7,7)
blur = cv.GaussianBlur(img,matrix,0)
cv.imshow('Blurred',blur)
cv.waitKey(0)
cv.destroyAllWindows()
