# from re import I
import cv2
import jso
from datetime import datetime
from easyocr import Reader
import os

lis = []
l = []

c = 1
def proces():
    dic = {
        'Name':'-',
        'Father Name':'-',
        'Gender':'-',
        'Country of Stay':'Pakistan',
        'Identity Number':'-',
        'Date of Birth':'-',
        'Date of Issue':'-',
        'Date of Expiry':'-'
        }
    
    reader = Reader(['en'])
    if os.path.isfile(r'recorded_video/output.avi'):
        cap = cv2.VideoCapture(r'recorded_video/output.avi')
    else:
        return 'Streaming Not found record again'
    while True:
        global c
        c+=1
        if c % 10 == 0:
            print('enter')
            ret,fram = cap.read()
            if ret == 0:
                break
            results = reader.readtext(fram)
            if '-' in dic.values():  
                print(dic.values)  
                for i in range(len(results)):
                    if results[i][2] > 0.8:
                        print(results[i][2])
                        print(results[i][1])
                        if  results[i][1] == 'Name' and dic['Name'] == '-':
                            dic[results[i][1]] = results[i+1][1]
                        if 'Father' in results[i][1]  and dic['Father Name'] == '-' and results[i+1][1] not in dic.keys():
                            dic['Father Name'] = results[i+1][1]

                        if results[i][1] not in dic.keys() and dic['Identity Number'] == '-' and len(results[i][1].split('-'))==3 and len(results[i][1])==15:
                            dic['Identity Number'] = results[i][1]
                            
                        if results[i][1] not in dic.keys() and '.' not in results[i][1] and len(results[i][1].split('.'))==3 and len(results[i][1])==10 and len(lis)<3:
                            lis.append(results[i][1])

                            if len(lis)==3  and dic['Date of Birth'] == '-' and dic['Date of Issue'] == '-' and dic['Date of Expiry'] == '-':
                                lis.sort(key=lambda date: datetime.strptime(date, "%d.%m.%Y"))
                                dic['Date of Birth'],dic['Date of Issue'],dic['Date of Expiry'] = lis
                                print(lis)
                        print(dic)
                        if dic['Gender'] == '-':        
                            if  results[i][1] == 'M':
                                dic['Gender'] = 'M'
                            elif results[i][1] == 'F':
                                dic['Gender'] = 'F'
                            
                if len(l) == 0:
                    fra = face(fram)
            else:
                print('ok')
                break
            lis.clear() 
    # cap.release()
    if isinstance(dic,dict):
        jso.save_data(dic)
        cv2.imwrite(fr'static/images/{dic["Identity Number"]}.jpg',fra)
        return dic
    else:
        return {
            'Output':'Invalid! check came.py'
        }



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
        
        l.append('3')
        return f

        