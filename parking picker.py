import pickle

import cv2
import pickle

width,height=(158-50),(240-192)

try:
    with open('carParkingMarked','rb') as f:
        poslist=pickle.load(f)

except:
    poslist = []




def mouseClick(events,x,y,flags,param):
    if events == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i , pos in enumerate(poslist):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                poslist.pop(i)

    with open('carParkingMarked','wb') as f:
        pickle.dump(poslist,f)





while True:
    cv2.namedWindow('parking')
    img = cv2.imread('carParkImg.png')
    cv2.rectangle(img, (50, 192), (158, 240), (255, 0, 255), 3)

    for pos in poslist:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255, 0, 255),3)

    cv2.imshow('parking', img)


    cv2.setMouseCallback('parking',mouseClick)
    cv2.waitKey(1)




