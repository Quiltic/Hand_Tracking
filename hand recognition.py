import numpy as np
import cv2, os, math, time

#path for making images
path = os.getcwd()
path = path + "\Poses"



def pictures(TYPE):
    print('Start {}'.format(TYPE))
    
    cap = cv2.VideoCapture(0)
    img_counter = 0
    print('Ready!')
    #top of the right hand
    righthand_top = 100
    #fatthest point to the right
    righthand_Far = 60

    #locations for points listed above
    farpoint = [60,0]
    toppoint = [0,100]

    #the loooooppppp
    while(img_counter < 101):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #""" 
        #640 by 480 picture for my laptop cam
        #Achual image is between 60 and 420 vertical
        cv2.imshow("full",frame)

        #what is used in all the achual processes
        mainframe = []
        
        #so it doesent go off the screen and crash
        if righthand_top < 60:
            righthand_top = 60
        if righthand_Far > 400:
            righthand_Far = 400
        if righthand_Far < 0 :
            righthand_Far = 0


        #get the virtical portions
        frame = frame[righthand_top:righthand_top+220]
        #get the horizontal
        for pt in range(len(frame)):
            #print(x, len(frame[pt][x:]))
            mainframe.append(frame[pt][righthand_Far:righthand_Far+240])
        #make it into an achual np array for cv2
        mainframe = np.array(mainframe)

        #My skin tone is between (229, 194, 198) and (116, 71, 74)
        #"""
        
        #dont know if this is needed but i dont want to risk it
        rgb = cv2.cvtColor(mainframe, cv2.COLOR_BGR2RGBA)

        lower = np.array([116, 71, 74, 255])
        upper = np.array([255, 194, 198, 255])

        #Threshold to get he achual skin and not walls (sorta)
        mask = cv2.inRange(rgb, lower, upper)

        #get the highest up point, and the farthest right
        fini = False
        winner = 4000
        for y in range(120): #normaly 240 but we dont realy look at the bottom 60
            for x in range(240):
                pixel = mask[y][x]
                #Im using the mask which meens I only need to find the white pixels
                if pixel == 255:
                    #for top point
                    if not (fini):
                        if y < 10:
                            righthand_top = (y-110) + righthand_top
                            toppoint = [x,y]
                            fini = True
                        elif y > 30:
                            righthand_top = (y-110) + righthand_top
                            toppoint = [x,y]
                            fini = True
                        else:
                            fini = True

                        if (y < 60):
                            break

                    #for farthest right
                    if (y >=60):
                        if x < 20:
                            if winner > x:
                                winner = x
                                farpoint = [x,y]
                            break
                        elif x > 80:
                            if winner > x:
                                winner = x
                                farpoint = [x,y]
                            break
                        else:
                            break

        #in case of falure
        if winner < 100:
            #this just works dont ask me why or how
            righthand_Far = (winner-60) + righthand_Far
        #"""
                        

        # Bitwise-AND mask and original image
        #res = cv2.bitwise_and(mainframe,mainframe, mask= mask)

        cv2.imshow('frame',mainframe)
        cv2.imshow('mask',mask)
        #cv2.imshow('res',res)




        #used for clicking
        dis = math.sqrt((toppoint[0]-farpoint[0])**2 + (toppoint[1]-farpoint[1])**2)
        
        if (dis < 25):
            print("click", dis)

        #print(toppoint,farpoint, dis)


        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        
    cap.release()
    cv2.destroyAllWindows()

pictures('face')
