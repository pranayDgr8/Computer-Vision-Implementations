import cv2
import imutils as imutils
import mediapipe as mp
import time
import PoseModule
mpPose=mp.solutions.pose
pose=mpPose.Pose()
cap=cv2.VideoCapture('E:\Pranay.mp4')#provide video file location or use the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,50)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,50)

pTime=0
mphands=mp.solutions.hands
hands= mphands.Hands
mpDraw=mp.solutions.drawing_utils
while True:
    success,img=cap.read()
    img=imutils.resize(img,width=400)
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(imgrgb)
    #print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            print(id,lm)
            cx,cy=int(lm.x*w),int(lm.y*h)
            cv2.circle(img,(cx,cy),3,(255,100,0),cv2.FILLED)


    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)




