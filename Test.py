import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    # define range of blue color in HSV
    
    #top = np.uint8([[[255,241,230]]])
    #hsv_top = cv2.cvtColor(top,cv2.COLOR_BGR2HSV)
    
    #bot = np.uint8([[[116,71,74]]])
    #hsv_bottom = cv2.cvtColor(bot,cv2.COLOR_BGR2HSV)
    #print (hsv_top,hsv_bottom)

    
    lower_blue = np.array([116, 71, 74, 255])
    upper_blue = np.array([255, 194, 198, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(rgb, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print("Escape hit, closing...")
        break
        
cap.release()
cv2.destroyAllWindows()