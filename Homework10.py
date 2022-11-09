
############### !!!! Answers to the questions #####################
CSRT is definitely slower than KCF
CSRT is trying to find the target anywhere on the screen when it is lost and sometimes act paranoic
KFC easily lose the target when the size changes (distance gets larger)
In order to show CSRT in action, I had to use more frames - 25
Please find uploaded frames in https://github.com/Valeriy77/cv_training/Frames
Please find original video in https://github.com/Valeriy77/cv_training/Frames
####################################################################
import cv2
import time
from PIL import Image

############### Tracker Types #####################

#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMIL_create()
tracker = cv2.TrackerKCF_create()
#tracker = cv2.TrackerTLD_create()
#tracker = cv2.TrackerMedianFlow_create()
#tracker = cv2.TrackerCSRT_create()
#tracker = cv2.TrackerMOSSE_create()

########################################################


cap = cv2.VideoCapture('C:\\Users\\vlazarenko\\Desktop\\!cv\\lesson_10\\v1.avi')
# TRACKER INITIALIZATION
success, frame = cap.read()
#bbox = cv2.selectROI("Tracking",frame, False)

bbox = [174, 99, 39, 29]
tracker.init(frame, bbox)
counter = 0

def drawBox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    cv2.putText(img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    if counter == 1 :
        print(x,y,w,h)

#TrackerKCF
while True:
    counter = counter +1
    time.sleep(0.5)
    timer = cv2.getTickCount()
    success, img = cap.read()
    success, bbox = tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.rectangle(img,(15,15),(200,90),(255,0,255),2)
    cv2.putText(img, "KCF Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 2);
    cv2.putText(img, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2);

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    if fps>60: myColor = (20,230,20)
    elif fps>20: myColor = (230,20,20)
    else: myColor = (20,20,230)
    cv2.putText(img,str(int(fps)), (90, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);

    im = Image.fromarray(img)
    im.save(r'frameKCF_' + str(counter) + '.jpg')

    cv2.imshow("Tracking", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
       break
    if counter > 14:
       break    


#Tracker2 CSRT ###################################


tracker = cv2.TrackerCSRT_create()

cap = cv2.VideoCapture('C:\\Users\\vlazarenko\\Desktop\\!cv\\lesson_10\\v1.avi')
# TRACKER INITIALIZATION
success, frame = cap.read()
#bbox = cv2.selectROI("Tracking",frame, False)

bbox = [174, 99, 39, 29]
tracker.init(frame, bbox)
counter = 0

while True:
    counter = counter +1
    time.sleep(0.5)
    timer = cv2.getTickCount()
    success, img = cap.read()
    success, bbox = tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.rectangle(img,(15,15),(200,90),(255,0,255),2)
    cv2.putText(img, "CSRT Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 2);
    cv2.putText(img, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2);

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    if fps>60: myColor = (20,230,20)
    elif fps>20: myColor = (230,20,20)
    else: myColor = (20,20,230)
    cv2.putText(img,str(int(fps)), (95, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);

    im = Image.fromarray(img)
    im.save(r'frameCSRT_' + str(counter) + '.jpg')

    cv2.imshow("Tracking", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
       break
    if counter > 24:
       break        