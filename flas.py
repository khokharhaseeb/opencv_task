from flask import Flask,render_template,Response,request,redirect,url_for,flash
import came
import os
from werkzeug.utils import secure_filename
import reco
import recording
import selfie_extraction as s
t = ''

    
app = Flask(__name__) 

UPLOAD_FOLDER = r'static\uploaded_images'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


      
@app.route("/")
def front():
    recording.release_camera()
    return render_template('home.html')
    

@app.route("/jso")
def showdata(i,img):
    
    import json
    folder = 'id_card_data'
    for a in os.listdir(folder):
        if a.split('.')[0] == i.split('.')[0]:
            file = os.path.join(folder,a)
            f = open(file)
            break
    data = json.load(f)
    img = f'uploaded_images/{img}'
    if isinstance(data,dict):
        return render_template("data.html",dic = data,im = img)
    
    else:
        return f'data sahi nahi print howa'

@app.route("/camera")
def camer():
    recording.release_camera()
    a = came.proces()
    
    b = s.proc()
    pro(b)
    
    if isinstance(a,dict):
        return render_template("data.html",dic = a)
    else:
        return f'Your video is not returning a valid responce and it is the response{a} try to record again or check your function name'
    
@app.route('/recoo')
def rec():
    global t 
    t = 'recorded_video'
    return render_template('index.html',next = 'sel')
@app.route('/recooo')
def sel():
    global t 
    t = 'selfie_video'
    return render_template('index.html',next = 'camer')
    
@app.route('/video_feed')
def video_feed():
    global t
    return Response(recording.cam(t), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/r')
def pro(filename):
        if not os.path.exists('static\images'):
            return 'first generate the data "No folder for data to match"'
        if len(os.listdir('static\images')) == 0:
            return 'No data to match first creat data thann uplaod image for matching '
        path_img = 'static\images'
        data_img = os.listdir('static\images')
        test = r'static\uploaded_images'
        test_img = os.path.join(test,filename)
        check = False
        for i in data_img:
            img = os.path.join(path_img,i)
            a = reco.recognition(img,test_img)
            if  a[0] == True:
                check = True
                matched_file = i
                break
        if check == True:
            return showdata(matched_file,filename)
        else:
            return 'Not Matched'

@app.route("/imagesubmit", methods=['GET', 'POST'])
def imagesubmit():
    if request.form.get('submit') == 'submit':
        f = request.files['image']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pro(filename)

if __name__=='__main__':
    
    app.run(debug=True)
