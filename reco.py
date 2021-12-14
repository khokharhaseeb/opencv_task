# import face_recognition

# def recognition(img,test_img):
    
#     known_image = face_recognition.load_image_file(img)
#     unknown_image = face_recognition.load_image_file(test_img)
#     biden_encoding = face_recognition.face_encodings(known_image)[0]
#     unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
#     # print('unknown',unknown_encoding)

#     results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
#     return results

# # just for testing
# # i = r'static\images\id.jpg'
# # t = r'uploaded_images\My_DP.jpg'
# # print(recognition(i,t))
from multiprocessing import Process
import time
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)
if __name__ == '__main__':
    start = time.time()
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    end = time.time() - start
    print(end)
    
    