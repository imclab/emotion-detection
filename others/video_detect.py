import cv2
 
TRAINSET = "/home/kaushal/Documents/Vedio2Text/jake/external/OpenCV-2.4.3/data/lbpcascades/lbpcascade_frontalface.xml"
DOWNSCALE = 4
 
webcam = cv2.VideoCapture('../capture.avi')
print webcam
cv2.namedWindow("preview")
classifier = cv2.CascadeClassifier(TRAINSET)
 
 
if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False
print rval 
while rval:
 
    # detect faces and draw bounding boxes
    minisize = (frame.shape[1]/DOWNSCALE,frame.shape[0]/DOWNSCALE)
    miniframe = cv2.resize(frame, minisize)
    faces = classifier.detectMultiScale(miniframe)
    for f in faces:
        x, y, w, h = [ v*DOWNSCALE for v in f ]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255))
 
    cv2.putText(frame, "Press ESC to close.", (5, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
    cv2.imshow("preview", frame)
 
    # get next frame
    rval, frame = webcam.read()
 
    key = cv2.waitKey(20)
    if key in [27, ord('Q'), ord('q')]: # exit on ESC
        break
