import sqlite3

import matplotlib.pyplot as plt
from tkinter import *
from playsound import playsound
import os
import datetime;
from PIL import ImageTk,Image
root=Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

#root.configure(background="white")

c=[]
d=[]
n=int(input("enter roll no"))
t=n
conn=sqlite3.connect("Face.db")
cmd="select avg(marks) from report"
cursor=conn.execute(cmd)
for row in cursor:
    c.append(row[0])
conn.commit()
conn.close()
a=round(c[0],2)

conn=sqlite3.connect("Face.db")
cmd="select marks from report where id=" +str(n)
cursor=conn.execute(cmd)
for row in cursor:
    d.append(row[0])
conn.commit()
conn.close()
o=round(d[0],2)

conn=sqlite3.connect("Face.db")
cmd="select attendance from report where id=" +str(n)
cursor=conn.execute(cmd)
for row in cursor:
    d.append(row[0])
conn.commit()
conn.close()
r=round(d[1],2)


g=[]
conn=sqlite3.connect("Face.db")
cmd="SELECT avgp FROM week"
    
cursor=conn.execute(cmd)
for row in cursor:
    g.append(row[0])
    

fig=plt.figure(1)
plt.bar(['Avg'],[a],label="Average Marks",color='b')
plt.bar(['MM'],[100],label="Maximum Marks",color='y')
plt.bar(['OM'],[o],label="Obtain Marks",color='g')
plt.legend()
plt.xlabel('x')
plt.ylabel('percentage')

plt.title("marks comparision")
plt.savefig('marks comparision')
fig=plt.figure(2)
plt.bar(['attendance'],[r],color='b')
plt.bar(['marks'],[o],color='g')
plt.legend()
plt.xlabel('x')
plt.ylabel('percentage')

plt.title("attendance vs marks")
#plt.show()
plt.savefig('attendance vs marks.png')

fig=plt.figure(3)
plt.bar(['mon','tues','wed','thu','fri','sat','sun'],g,color='b')
plt.legend()
plt.xlabel(datetime.date.today())
plt.ylabel('percentage')


plt.title("weekly attendance ")
plt.savefig('weekly attendance')
n=datetime.date.today().weekday()
if n==6:
    conn=sqlite3.connect("Face.db")
    cmd="update week set avgp=0"
    
conn.execute(cmd)
conn.commit()
conn=sqlite3.connect('face.db')
cmd='select name from peoples where id=' +str(t)
cursor=conn.execute(cmd)
for row in cursor:
    s=(row[0])

var1 = StringVar()
var1.set(str(t))

var2 = StringVar()
var2.set(str(s))

def fun():
    Image.open("weekly attendance.png").show()
    
        
root.title("Performance")

Label(root,text='Roll no:  ',font=('freesansbold',25),pady=5,padx=5).grid(sticky = W,row=0,column=0)
Label(root,textvariable =var1,font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=0,column=1)

Label(root,text='Name:     ',font=('freesansbold',25),pady=5,padx=5).grid(sticky = W,row=1,column=0)
Label(root,textvariable =var2,font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=1,column=1)
  


img1 = ImageTk.PhotoImage(Image.open("attendance vs marks.png"))       
Label(root,image=img1).grid(sticky=W,row=3,column=0)
img2 = ImageTk.PhotoImage(Image.open("marks comparision.png"))       
Label(root,image=img2).grid(sticky=E,row=3,column=4)
Label(root,text=' weekly performance of class:  ',font=('freesansbold',25),pady=5,padx=5).grid(sticky = W,row=10,column=0)
Button(root,text = 'Click',bd = 3 ,font = ('freesansbold',15),padx=5,pady=5,command=fun).grid(sticky=W,row=10,column=1)
root.mainloop()
