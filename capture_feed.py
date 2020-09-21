import os
import cv2
from mss import mss
import numpy as np
import time

def preprocessing(img):
    img = img[::,75:615]
    img = cv2.Canny(img, threshold1=100, threshold2=200)
    return img

# captures dinosaur run game, designed for my personal computer (adjust coordinates resepctively)
def start():
    """
    Captures video feed frame by frame, crops out unecessary dino and processes
    """
    startingpoint_obj = open('D:/DBD_ML/starting.txt','r')
    startingpoint = int(startingpoint_obj.read())
    startingpoint_obj.close()
    sct = mss()

    coordinates = {
        'top': 450,
        'left': 800,
        'width': 245,
        'height': 190,
    }

    fileexists = False
    control=0
    with open('D:/DBD_ML/actions_automated.csv', 'r',newline="") as csv:
        a = csv.readline(1)
        print(a)
        if a=="0" or a=="1":
            fileexists = True

    if fileexists:
        with open('D:/DBD_ML/actions_automated.csv', 'a',newline="") as csv:

            x = startingpoint
            img = preprocessing(np.array(sct.grab(coordinates)))
            prev_pic = img
            if not os.path.exists(r'D:/DBD_ML/auto_db'):
                os.mkdir(r'D:/DBD_ML/auto_db')
            while control<100000:
                time.sleep(0.05)
                img_old = img

                img = preprocessing(np.array(sct.grab(coordinates)))


                if (img_old==prev_pic).all()!=True and (img_old==0).all()!=True:

                    if (img_old==img).all():
                        prev_pic = img_old
                        cv2.imwrite('D:/DBD_ML/auto_db/frame_{0}.jpg'.format(x), img_old)
                        csv.write('1\n')
                        print('space write')
                        x += 1
                        control += 1
                        print(x)
                    else:
                        prev_pic = img_old
                        cv2.imwrite('D:/DBD_ML/auto_db/frame_{0}.jpg'.format(x), img_old)
                        csv.write('0\n')
                        print('none write')
                        x += 1
                        control += 1


                # break the video feed

            endpoint_obj = open('D:/DBD_ML/starting.txt', 'w')
            endpoint_obj.write(str(x))
            print(str(x))
            endpoint_obj.close()
            csv.close()
            cv2.destroyAllWindows()
    else:
        with open('D:/DBD_ML/actions_automated.csv', 'w',newline="") as csv:

            x = startingpoint
            img = preprocessing(np.array(sct.grab(coordinates)))
            prev_pic = img
            if not os.path.exists(r'D:/DBD_ML/auto_db'):
                os.mkdir(r'D:/DBD_ML/auto_db')
            while control<100000:
                time.sleep(0.05)
                img_old = img

                img = preprocessing(np.array(sct.grab(coordinates)))


                if (img_old==prev_pic).all()!=True and (img_old==0).all()!=True:

                    if (img_old==img).all():
                        prev_pic = img_old
                        cv2.imwrite('D:/DBD_ML/auto_db/frame_{0}.jpg'.format(x), img_old)
                        csv.write('1\n')
                        print('space write')
                        x += 1
                        control += 1
                        print(x)
                    else:
                        prev_pic = img_old
                        cv2.imwrite('D:/DBD_ML/auto_db/frame_{0}.jpg'.format(x), img_old)
                        csv.write('0\n')
                        print('none write')
                        x += 1
                        control += 1


                # break the video feed

            endpoint_obj = open('D:/DBD_ML/starting.txt', 'w')
            endpoint_obj.write(str(x))
            print(str(x))
            endpoint_obj.close()
            csv.close()
            cv2.destroyAllWindows()


#9.33% der Anzahl der Frames ist Anzahl der Skillchecks
#2,626 sec ist die Zeit zwischen 2 Skillchecks


start()