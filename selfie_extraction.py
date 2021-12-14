import cv2
import os
def proc():
    if os.path.isfile(r'selfie_video/output.avi'):
        cap = cv2.VideoCapture(r'selfie_video/output.avi')
    else:
        return 'video not found'
    while True:
       
        ret,fram = cap.read()
        
        if ret == 0:
            break
        b = face(fram)
        if b != False:
            break
    return b
def face(fram):
    face_c = cv2.CascadeClassifier('h.xml')
    f = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    box,det = face_c.detectMultiScale2(f)
    print('box',box)
    print(det)
    if len(det) > 0 and det[0] >= 80:
        x = box[0][0]
        y = box[0][1]
        w = box[0][2]
        h = box[0][3]
        x = x-25
        y = y-25
        w = w+x+45
        h = h+y+30
        f = fram[y:h,x:w]
        n = 'self.jpg'
        cv2.imwrite(n,f)
        return n 
    else:
        return False