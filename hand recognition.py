import numpy as np
import cv2, os


path = os.getcwd()
path = path + "\Poses"
def pictures(TYPE):
    print('Start {}'.format(TYPE))
    cap = cv2.VideoCapture(0)
    img_counter = 0
    print('Ready!')
    while(img_counter < 101):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',grey)
        

        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        if img_counter > 30:
            img_name = "hand_{}_{}.png".format(TYPE,img_counter-30)
            cv2.imwrite(os.path.join(path , img_name), frame)
            print("{} written!".format(img_name))
        img_counter += 1

    cap.release()
    cv2.destroyAllWindows()

pictures('face')
