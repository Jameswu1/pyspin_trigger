import EasyPySpin
import time
import cv2
import datetime
import os

def makedaliyfile():
    path =  str(datetime.date.today())
    path1 = path + "/AA_DL"
    if not os.path.isdir(path):
        os.mkdir(path)
    if not os.path.isdir(path1):
        os.mkdir(path1)

def makecarfile():
    loc_dt = datetime.datetime.today() 
    #time_del = datetime.timedelta(hours=8)
    #loc_dt = loc_dt + time_del
    path1 =  str(datetime.date.today())
    path2 = loc_dt.strftime("%H-%M-%S")
    path = path1 + "/AA_DL/" + str(path2)
    if not os.path.isdir(path):
        os.mkdir(path)
    return str(path1),str(path2)


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

    while(cap.isOpened()):
        #print(cap.isOpened())
        ret,frame = cap.read()
        #print(k)
        #print(cap.get(cv2.CAP_PROP_TRIGGER))
        #if ret == False:
        #    k = 1
        #    continue
        #if k == 1:
        if k == 50:
            break
        #day,time = makecarfile()
        img_show = cv2.resize(frame, None, fx=0.25, fy=0.25)
        #path = day + "/AA_DL/" + time + "/" + str(k) + ".jpg"
        path = str(k) + ".jpg"
        cv2.imwrite(path,frame)
        k += 1

        cv2.imshow("Q",img_show)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
