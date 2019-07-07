import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);


def insertOrUpdate(Id,name,age,des):
    conn=sqlite3.connect("Face.db")
    cmd="SELECT * FROM  Peoples WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0;
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE Peoples SET Name="+str(name)+" WHERE ID="+str(Id)
        cmd="UPDATE Peoples SET Age="+str(age)+" WHERE ID="+str(Id)
        cmd="UPDATE Peoples SET Designation="+str(des)+" WHERE ID="+str(Id)
        
    else:
        cmd="INSERT INTO Peoples(ID,Name,Age,Designation,presence) VALUES("+str(Id)+" ,"+str(name)+","+str(age)+","+str(des)+","+str(0)+")"
        #cmd="INSERT INTO Totals(ID,Name,pr) VALUES("+str(Id)+" ,"+str(name)+","+str(0)+")"

        
    conn.execute(cmd)
    conn.commit()
    conn.close()
    conn=sqlite3.connect("Face.db")
    cmd="SELECT * FROM  totals WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0;
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE totals SET Name="+str(name)+" WHERE ID="+str(Id)
        cmd="UPDATE totals SET Attended="+str(0)+" WHERE ID="+str(Id)
        cmd="UPDATE totals SET pr="+str(0)+" WHERE ID="+str(Id)
        cmd="Update totals set percentage="+str(0)+" where id="+str(Id)
                        
    else:
        #cmd="INSERT INTO Peoples(ID,Name,Age,Designation,presence) VALUES("+str(Id)+" ,"+str(name)+","+str(age)+","+str(des)+","+str(0)+")"
        cmd="INSERT INTO Totals(ID,Name,attended,pr,percentage) VALUES("+str(Id)+" ,"+str(name)+","+str(0)+","+str(0)+","+str(0)+")"
        
        
    conn.execute(cmd)
    conn.commit()
    conn.close()


    conn=sqlite3.connect("Face.db")
    cmd="SELECT * FROM  report WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0;
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE report SET Name="+str(name)+" WHERE ID="+str(Id)
        
                        
    else:
        #cmd="INSERT INTO Peoples(ID,Name,Age,Designation,presence) VALUES("+str(Id)+" ,"+str(name)+","+str(age)+","+str(des)+","+str(0)+")"
        cmd="INSERT INTO report(ID,Name) VALUES("+str(Id)+" ,"+str(name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id=input("enter user id")
name=input("enter your name")
age=input("enter age")
des=input("enter designation")
insertOrUpdate(id,name,age,des)
sampleNum=0
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        
        cv2.imwrite("dataSet/user."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.waitKey(100);
    cv2.imshow("FACE",img);
    cv2.waitKey(1);
    if(sampleNum>100):
            break
cam.release()
cv2.destroyAllWindows()
#conn=sqlite3.connect("Face.db")
#cmd="INSERT INTO Totals(ID,Name) SELECT ID,Name FROM PEOPLES"
#conn.execute(cmd)
#conn.commit()
#conn.close()
