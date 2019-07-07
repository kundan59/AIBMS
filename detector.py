import cv2
import numpy as np
import sqlite3
import sys
import xlwt
import datetime
import requests
c=[]
conn=sqlite3.connect("Face.db")
cmd="UPDATE Peoples SET PRESENCE='0' WHERE PRESENCE=1"
cursor=conn.execute(cmd)
conn.commit()
conn.close()
 
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("recognizer\\trainningData.yml")
id=0
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (0, 255, 0)
i=0
def getProfile(id):
    conn=sqlite3.connect("Face.db")
    cmd="SELECT * FROM PEOPLES WHERE ID="+str(id)
    
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile
    

while(i<=40):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if profile!=None:
            i=i+1
            conn=sqlite3.connect("Face.db")
            cmd="UPDATE Peoples SET PRESENCE="+str(i)+" WHERE ID="+str(id)
            
            cursor=conn.execute(cmd)
            conn.commit()
            conn.close()
            
            
            
            conn.close()
            if conf<1000:    
                cv2.putText(img,"name="+str(profile[1]),(x,y+h+30),fontface,fontscale,fontcolor);
                cv2.putText(img,"age="+str(profile[2]),(x,y+h+60),fontface,fontscale,fontcolor);
                cv2.putText(img,"designation="+str(profile[3]),(x,y+h+90),fontface,fontscale,fontcolor);
                
                
            else:
                cv2.putText(img,"unknown",(x,y+h+30),fontface,fontscale,fontcolor);
                
                
                
       
            
            
            
                
            
    cv2.imshow("FACE",img);
    
    if(cv2.waitKey(1)==ord('q')):
        break;
if i>0: 
    conn=sqlite3.connect("Face.db")
    
    cmd="UPDATE Peoples SET PRESENCE="+"1"+" WHERE PRESENCE > "+ "0"
    
    cursor=conn.execute(cmd)
    conn.commit()
    conn.close()
    conn=sqlite3.connect("Face.db")
else:
    conn=sqlite3.connect("Face.db")
    
    cmd="UPDATE Peoples SET PRESENCE="+"0"
    
    cursor=conn.execute(cmd)
    conn.commit()
    conn.close()
    conn=sqlite3.connect("Face.db")
    

    
   

    


conn=sqlite3.connect("Face.db")
cmd='SELECT COUNT(ID) FROM PEOPLES'
cursor=conn.execute(cmd)
prf=None
for row in cursor:
    prf=row
conn.close()
a=prf[0]
#print((prf[0]))

conn=sqlite3.connect("Face.db")
cmd="SELECT sum(presence) FROM  peoples" 
cursor=conn.execute(cmd)
for row in cursor:
    
    c.append(row[0])
conn.execute(cmd)
conn.commit()

workbook = xlwt.Workbook()  
sheet = workbook.add_sheet("Sheet Name") 
style = xlwt.easyxf('font: bold 1,color blue;') 
sheet.write(0, 0, 'ID', style)
sheet.write(0, 1, 'NAME', style)
sheet.write(0, 2, 'PRESENCE', style)
sheet.write(0, 3, 'DATE', style)
sheet.write(0, 7, 'Total', style)
style1 = xlwt.easyxf('font: bold 0,color black;')
for i in range(1,a+1):
    conn=sqlite3.connect("Face.db")
    cmd='SELECT ID FROM PEOPLES WHERE ID='+str(i)
    cursor=conn.execute(cmd)
    cm=None
    for row in cursor:
        cm=row
    conn.close()
    sheet.write(i,0,cm[0],style1)

for i in range(1,a+1):
    conn=sqlite3.connect("Face.db")
    cmd='SELECT NAME FROM PEOPLES WHERE ID='+str(i)
    cursor=conn.execute(cmd)
    cm=None
    for row in cursor:
        cm=row
    conn.close()
    sheet.write(i,1,cm[0],style1)

for i in range(1,a+1):
    conn=sqlite3.connect("Face.db")
    cmd='SELECT PRESENCE FROM PEOPLES WHERE ID='+str(i)
    cursor=conn.execute(cmd)
    cm=None
    for row in cursor:
        cm=row
    conn.close()
    sheet.write(i,2,cm[0],style1)

for i in range(1,a+1):
    
    sheet.write(i,3,str(datetime.datetime.now()),style1)

sheet.write(2,7,c[0],style)        
            
workbook.save("attendance.xls")
conn=sqlite3.connect("Face.db")


cmd="UPDATE Totals SET Total=" "Total" "+" "1"
#cmd="UPDATE Totals SET Attended=" "(select (Peoples.presence + Totals.Attended) from peoples,totals" +" WHERE Peoples.ID = "+ "Totals.ID"+")"
conn.execute(cmd)
conn.commit()
conn.close()

conn=sqlite3.connect("Face.db")


cmd="UPDATE Totals set pr=(select presence from peoples where totals.id=peoples.id)"
conn.execute(cmd)
conn.commit()
conn.close()

conn=sqlite3.connect("Face.db")
cmd="SELECT * FROM  totals" 
cursor=conn.execute(cmd)
for row in cursor:
    
    cmd="UPDATE Totals SET Attended=" "(attended + pr)"
conn.execute(cmd)
conn.commit()
conn.close()

conn=sqlite3.connect("Face.db")
cmd="SELECT id,attended,total FROM  totals" 
cursor=conn.execute(cmd)
for row in cursor:
    
    #print(r)
    
    cmd="update totals set percentage="+str(round((row[1]/row[2])*100))+" where id="+str(row[0]) 
    conn.execute(cmd)
    conn.commit()
conn.close()


conn=sqlite3.connect("Face.db")
cmd="SELECT id,attended,total FROM  totals" 
cursor=conn.execute(cmd)
for row in cursor:
    
    #print(r)
    
    cmd="update report set attendance="+str(round((row[1]/row[2])*100))+" where id="+str(row[0]) 
    conn.execute(cmd)
    conn.commit()
conn.close()

c=[]
conn=sqlite3.connect("Face.db")
cmd="SELECT sum(presence),count(id) FROM  peoples" 
cursor=conn.execute(cmd)
for row in cursor:
    
    c.append(row[0])
    c.append(row[1])
    
 
conn.execute(cmd)
conn.commit()
a=round((c[0]/c[1])* 100)
#day=['monday','tuesday','wednesday','thrusday','friday','saturday','sunday']
n=int(datetime.datetime.today().weekday())



conn=sqlite3.connect("Face.db")
cmd="update week set avgp="+str(a)+" where days="+str(n) 
conn.execute(cmd)
conn.commit()




conn=sqlite3.connect("Face.db")
cmd="select mnumber from peoples where presence=0"

cursor=conn.execute(cmd)
for row in cursor:
    pr=row[0]
    #print(type(pr))
    #print(pr)
    
    url = "https://www.fast2sms.com/dev/bulk"
 
    payload = "sender_id=FSTSMS & message= Dear parent your ward is not present in classroom. & language=english & route=p & numbers="+str(pr)
    headers = {
     'authorization': "zg6YJqFs2wCbPGM9H5p4QOiDlSAca7KvIhWrLxNmEX0RoVBdkefWOGmNVHeR9d6lM8Kzn07gQPBhusFU",
     'Content-Type': "application/x-www-form-urlencoded",
     'Cache-Control': "no-cache",
     }
 
    response = requests.request("POST", url, data=payload, headers=headers)
 
    print(response.text)


conn.commit()
conn.close()





cam.release()
cv2.destroyAllWindows()

    
