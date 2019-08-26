import numpy as np
import cv2, os, math, time


path = os.getcwd()
path = path + "\Poses"

def comparehighlow(high,low,inpt):
    if (inpt <= high) and (inpt >= low):
        return(True)
    return(False)


def pictures(TYPE):
    print('Start {}'.format(TYPE))
    
    cap = cv2.VideoCapture(0)
    img_counter = 0
    print('Ready!')
    righthand_top = 100
    righthand_Far = 60
    #righthand_Mid = 300
    farpoint = [60,0]
    toppoint = [0,100]
    while(img_counter < 101):
        # Capture frame-by-frame
        ret, frame = cap.read()
        """
        home = []
        for cubey in range(8):
            row = []            
            for cubex in range(8):
                blob = np.array([0,0,0])
                for y in range(30):
                    for x in range(30):
                        pixel = frame[cubey*30+y+righthand_top][cubex*30+x+righthand_Far]
                        blob += pixel
                
                blob = blob/400
                row.append(blob)
            home.append(np.array(row))
        home = np.array(home)
        #print(home)
        #cv2.imwrite("Ohhhh.png", home)
        #break
        #"""    
        """
        for y in range(8):
            for x in range(8):
                pixel = home[y][x]
                if comparehighlow(255,110,pixel[0]):
                    if comparehighlow(240,75,pixel[1]):
                        if comparehighlow(229,70,pixel[2]):
                            righthand_top = y*30
                            print(pixel)
                            break 
        #"""
        
        
        """
        #origonal thing to get hand position
        #240 by 240
        for y in range(240):
            for x in range(righthand_Mid-righthand_Far):
                pixel = frame[y+righthand_top][x+righthand_Far]
                if comparehighlow(255,110,pixel[0]):
                    if comparehighlow(240,75,pixel[1]):
                        if comparehighlow(229,70,pixel[2]):
                            righthand_top = y
                            print(pixel)
                            break 
        #"""
        #"""        
        #640 by 480
        #Achual image is between 60 and 420 vertical

        cv2.imshow("full",frame)


        mainframe = []
        
        if righthand_top < 60:
            righthand_top = 60
        
        if righthand_Far > 620:
            righthand_Far = 620
        if righthand_Far < 0 :
            righthand_Far = 0


        frame = frame[righthand_top:righthand_top+220]
        for pt in range(len(frame)):
            #print(x, len(frame[pt][x:]))
            mainframe.append(frame[pt][righthand_Far:righthand_Far+240])
        mainframe = np.array(mainframe)
        #My skin tone is between (229, 194, 198) and (116, 71, 74)
        # Our operations on the frame come here
        #"""
        
        rgb = cv2.cvtColor(mainframe, cv2.COLOR_BGR2RGBA)

        lower_blue = np.array([116, 71, 74, 255])
        upper_blue = np.array([255, 194, 198, 255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(rgb, lower_blue, upper_blue)

        #get the highest up point
        fini = False
        for y in range(len(mask)):
            for x in range(len(mask[y])):
                pixel = mask[y][x]
                if pixel == 255:
                    if y < 10:
                        righthand_top = (y-110) + righthand_top
                        toppoint = [x,y]
                        fini = True
                        break
                    elif y > 30:
                        righthand_top = (y-110) + righthand_top
                        toppoint = [x,y]
                        fini = True
                        break
                    else:
                        fini = True
                        break
            if fini:
                break
        #"""

        #get the farthest point to the right 
        winner = 4000
        for y in range(100):
            for x in range(len(mask[y])):
                pixel = mask[y+60][x]
                if pixel == 255:
                    if x < 10:
                        if winner > x:
                            winner = x
                            farpoint = [x,y]
                        break
                    elif x > 30:
                        if winner > x:
                            winner = x
                            farpoint = [x,y]
                        break
                    else:
                        break
        if winner < 60:
            righthand_Far = (winner-30) + righthand_Far
        #"""
                        

        # Bitwise-AND mask and original image
        #res = cv2.bitwise_and(mainframe,mainframe, mask= mask)

        cv2.imshow('frame',mainframe)
        cv2.imshow('mask',mask)
        #cv2.imshow('res',res)




        #used for clicking
        dis = math.sqrt((toppoint[0]-farpoint[0])**2 + (toppoint[1]-farpoint[1])**2)
        
        if (dis < 25):
            print("click", dis, timesincelastclicked)

        #print(toppoint,farpoint, dis)


        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        """
        if img_counter > 30:
            img_name = "hand_{}_{}.png".format(TYPE,img_counter-30)
            cv2.imwrite(os.path.join(path , img_name), frame)
            print("{} written!".format(img_name))
        img_counter += 1
        #"""
    cap.release()
    cv2.destroyAllWindows()

pictures('face')
