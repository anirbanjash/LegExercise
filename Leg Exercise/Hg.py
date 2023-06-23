import cv2
import numpy as np
import time
import Posemodule as pm
cap=cv2.VideoCapture(0)
import pandas as pd
#cap=cv2.VideoCapture(0)
detector=pm.poseDetector()
count=0
dir=0
pTime=0
while True:
    success,img=cap.read()
    # img=cv2.resize(img,(1280,720))
    img=cv2.resize(img,(640,480))
    img=detector.findPose(img,False)
    lmlist=detector.findPosition(img,False)
    #print(lmlist)
    if len(lmlist)!=0:
        point_20=[lmlist[20][1],lmlist[20][2]]
        point_6=[lmlist[6][1],lmlist[6][2]]
        point_19=[lmlist[19][1],lmlist[19][2]]
        point_3=[lmlist[3][1],lmlist[3][2]]
        
        # cv2.line(img,(point_19[0],point_19[1]),(point_3[0],point_3[1]),(255,0,0),5)
        left_dist=(((lmlist[19][1]-lmlist[3][1])**2)+((lmlist[19][2]-lmlist[3][2])**2))**(1/2)
        # print(left_dist)
        # cv2.line(img,(point_20[0],point_20[1]),(point_6[0],point_6[1]),(0,0,255),5)
        right_dist=(((lmlist[20][1]-lmlist[6][1])**2)+((lmlist[20][2]-lmlist[6][2])**2))**(1/2)
        # print(right_dist)

        left_knee_dist=((((lmlist[11][1]-lmlist[25][1])**2)+((lmlist[11][2]-lmlist[25][2])**2))**(1/2));
        # print(left_knee_dist)
        right_knee_dist=(((lmlist[12][1]-lmlist[26][1])**2)+((lmlist[12][2]-lmlist[26][2])**2))**(1/2)
        # print(right_knee_dist)
        # cv2.line(img,(point_20[0],point_20[1]),(point_19[0],point_19[1]),(0,0,255),5)
        
# ACCILARATIO  AND BREAK

        if (  left_dist<=140 and right_dist<=180 and left_knee_dist<=300):
            print("BHHAG MILKHA BHAAG")
        elif ( left_dist>140 and right_dist>180 and left_knee_dist>300):
            print("ASTEE KAKa ASTE")
    
    # RIDE SIDE LEFT SIDE CHANGE
        #LEFT arm
        right_angle=detector.findAngle(img,14,12,24,draw=True)
        # print(right_angle)
        left_angle=detector.findAngle(img,13,11,23,draw=True)
        # print(left_angle)
        if(right_angle<=290):
            print("Left e Jao")
        elif(left_angle>=75):
            print("Right e Jao")
            
        #   LATHI MARA FUNCTION 
    
        point_26=[lmlist[26][1],lmlist[26][2]]
        point_25=[lmlist[25][1],lmlist[25][2]]      
        left_right_hantu_dist=(((lmlist[26][1]-lmlist[25][1])**2)+((lmlist[26][2]-lmlist[25][2])**2))**(1/2)
        # print(left_right_hantu_dist)
        if(left_right_hantu_dist>180):
                print("MAR LATHI")
        color=(255,0,255)
        #CHECK DUMBLE CURLS
        # if angle>=270:
        #     print("Accelaration")
          
        # if angle<270:
        #     print("Break")
          
        # Draw bar
         
         
        #Draw curl count
        # cv2.rectangle(img,(0,450),(350,720),(155,255,0),cv2.FILLED)
        # cv2.putText(img,str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),20)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    # cv2.putText(img,str(int(fps)),(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),5)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
  