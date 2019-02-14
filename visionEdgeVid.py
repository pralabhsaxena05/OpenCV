import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    laplacian = cv.Laplacian(frame, cv.CV_64F)
    
    edges = cv.Canny(frame, 100, 150)

    cv.imshow('Original', frame)
    cv.imshow('edges', edges)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
    

cv.destroyAllWindows()
cap.release()
    
