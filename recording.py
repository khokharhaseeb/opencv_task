import cv2 
import os
camera =  cv2.VideoCapture()
def cam(t):  
    global camera 
    camera = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    if not os.path.exists(f'{t}'):
        os.mkdir(f'{t}')
    save = fr'{t}/output.avi'
    cap_rec = cv2.VideoWriter(save,fourcc,40.0,(640,480))
    while True:
        ret,frame=camera.read()
        if not ret:
            break
        cap_rec.write(frame)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
def release_camera():
    if camera.isOpened():
        camera.release()