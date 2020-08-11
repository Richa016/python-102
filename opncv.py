import cv2
import dropbox
import time
import random

def take_snapshot():
    number=random.randint(0,100)
    vidoeCapture = cv2.VideoCapture(0)
    result = True
    while (result):
        ret,frame =vidoeCapture.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshot taken")
    vidoeCapture.release()
    cv2.destroyAllWindows()
take_snapshot()

def upload_file(img_name):
    access_token='mckhB0VxLHAAAAAAAAAAAXPkd3r3FuZrQUftXferutpN10XCOkapfN02F5IXeuvp'
    file=img_counter
    file_from=file
    dile_to="/newFolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    
    with open(file_from,'rb') as f:
        dbx.files.upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploadED")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)
main()
