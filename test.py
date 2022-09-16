import EasyPySpin
import time
import cv2
import datetime
import os

def makedaliyfile():
    path =  str(datetime.date.today())
    if not os.path.isdir(path):
        os.mkdir(path)

def makecarfile():
    loc_dt = datetime.datetime.today() 
    #time_del = datetime.timedelta(hours=8)
    #loc_dt = loc_dt + time_del
    path1 =  str(datetime.date.today())
    path2 = loc_dt.strftime("%H-%M-%S")
    path = path1 + "/A_DL" + str(path2)
    if not os.path.isdir(path):
        os.mkdir(path)


def main():
    cap = EasyPySpin.VideoCapture(0)
    if not cap.isOpened():
        print("c not open")
        return -1
    cap.set(cv2.CAP_PROP_EXPOSURE, 1000)
    #cap.set(cv2.CAP_PROP_TRIGGER,True)
    cap.set(cv2.CAP_PROP_GAIN, -1)
    makedaliyfile()
    k = 1
    key_name = 1
    while(1):
   # while(cap.get(cv2.CAP_PROP_TRIGGER)):
        ret,frame = cap.read()
        date = datetime.date.today()
        img_show = cv2.resize(frame, None, fx=0.3, fy=0.3)

        #if k == 60:
        #    makecarfile()
        #    loc_dt = datetime.datetime.today() 
        #    path1 =  str(datetime.date.today())
        #    path2 = loc_dt.strftime("%H-%M-%S")
        #    path = path1 + "/" + str(path2) + "/" + str(k) + ".jpg"
        #    cv2.imwrite(path,img_show)
        #    k = 1
        #    key_name += 1
        #k += 1
        #path = datetime.datetime.today() 
        #path2 = path.strftime("%H-%M-%S")
        #path2 = str(path2) + "_" + str(k) + ".jpg"
        #cv2.imwrite(path2,img_show)

        cv2.imshow("Q",img_show)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
