import cv2
import time
import math

#Installed - pip install opencv-contrib-python==3.4.13.47
vid = cv2.VideoCapture("bb3.mp4")

tracker = cv2.TrackerCSRT_create()

ret, image = vid.read()

#Selection item of the video you want to track
bBox = cv2.selectROI("Tracking", image, False)

#Initiating the tracker on the image. Tracking bounding box, bBox.
tracker.init(image, bBox)

print(bBox)

def drawBox(img,boundingBox):
    x = int(boundingBox[0])
    y = int(boundingBox[1])
    width = int(boundingBox[2])
    height = int(boundingBox[3])
    cv2.putText(img,"Tracking..",(70,90),cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5, thickness=1, color=(0,0,255))
    cv2.rectangle(img, (x,y), (x+width,y+height),(0,0,255),4)

def goalTracking(img,boundingBox):
    x = int(boundingBox[0])
    y = int(boundingBox[1])
    width = int(boundingBox[2])
    height = int(boundingBox[3])
    
while True:
    bool, frame = vid.read()
    success, bBox = tracker.update(frame)
    if success:
        drawBox(frame, bBox)
    else:
        error = "We lost the object"
        cv2.putText(frame, error, (70,90),color=(0,0,255), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5, thickness=1)
    cv2.imshow("Basketball", frame)

    if cv2.waitKey(25) == 32:
        break

vid.release()
cv2.destroyAllWindows()