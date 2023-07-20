import cv2
import numpy as np
import cvzone
import pickle

width,height=(158-50),(240-192)
cap=cv2.VideoCapture('carPark.mp4')

with open('carParkingMarked', 'rb') as f:
    poslist = pickle.load(f)

def checkParkingSpace(imgPro):
    spacecounter = 0
    for pos in poslist:
        x,y=pos
        # cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255, 0, 255),3)
        # cv2.imshow('video', img)

        imgCrop=imgPro[y:y+height,x:x+width]
        # cv2.imshow((str(x+y)),imgCrop)
        count=cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img,str(count),(x,y+height-10),scale=1,thickness=2,offset=0,colorR=(0,0,255))
        if count<500:
            color=(0,255,0)
            thickness=5
            spacecounter=spacecounter+1

        else:
            color=(0,0,255)
            thickness=2


        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

    cvzone.putTextRect(img,f' free:{str(spacecounter)} | outoff:{len(poslist)}',(320,60),scale=2,thickness=2,offset=10,colorR=(0,0,0))


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold=cv2.adaptiveThreshold(imgblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                          cv2.THRESH_BINARY_INV,25,16)
    imgmedian=cv2.medianBlur(imgThreshold,5)
    kernal=np.zeros((3,3),np.uint8)
    imgDilate=cv2.dilate(imgmedian,kernal,iterations=1)

    checkParkingSpace(imgDilate)

    cv2.imshow('Image',img)
    # cv2.imshow('ImageBlur', imgblur)
    # cv2.imshow('imgthreshold',imgThreshold)
    # cv2.imshow('imgmedian', imgmedian)
    # cv2.imshow('imgDilate', imgDilate)
    cv2.waitKey(1)








