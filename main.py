from tkinter import *
from playsound import playsound
import os
from datetime import datetime;
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox as ms
#from graphs import t






class main():
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.widgets()
    def function1(self):
    
        os.system("python datasetCreator.py")
        playsound('sound.mp3')
    
    def function2(self):
    
        os.system("python trainner.py")
        playsound('sound.mp3')

    def function3(self):

        os.system("python detector.py")
        playsound('sound.mp3')


   
    def function6(self):

        window.destroy()

    def function7(self):
        os.system("python classify.py")
        playsound('sound.mp3')
    def function8(self):
        os.system("python report.py")
        playsound('sound.mp3')
    
    

    def attend(self):
        os.startfile("attendance.xls");

    def graph(self):
        os.system("python graphs.py")
        
        
        
        playsound('sound.mp3')

    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('freesansbold',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('freesansbold',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('freesansbold',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('freesansbold',15),padx=5,pady=5,command=self.login).grid(row=2,column=1)
        self.logf.pack()
        #self.logf.pack_forget()
        
        self.img1 = ImageTk.PhotoImage(Image.open("classroom.jpg"))
        self.im=Label(self.logf,image=self.img1).grid(column=1,row=5)
        self.im.pack()
        
        
        


    def login(self):
        with sqlite3.connect('face.db') as db:
            conn=db.cursor()
        cmd='SELECT * FROM password WHERE username = ? and password = ?'
        conn.execute(cmd,[(self.username.get()),(self.password.get())])
        result=conn.fetchall()
        if result:
            window.title("AIBMS")
            self.logf.pack_forget()
            self.head.pack_forget()
            self.goff = Frame(self.master,padx =10,pady = 10)
            #creating a text label
            Label(self.goff, text="          AI BASED MONITORING AND ASSISTENCE          ",font=("times new roman",30),fg="black",bg="orange",height=2).grid(row=0,sticky=N+E+W+S,padx=5,pady=5)


            Button(self.goff,text="   Registration     ",font=("times new roman",30),bg="#1B58B2",fg='white',command=self.function1).grid(row=2,sticky=W,padx=25,pady=25)

            #creating second button
            Button(self.goff,text="   Train Dataset   ",font=("times new roman",30),bg="#1B58B2",fg='white',command=self.function2).grid(row=4,sticky=W,padx=25,pady=25)

            #creating third button
            Button(self.goff,text="Mark Attendance",font=('times new roman',30),bg="#1B58B2",fg="white",command=self.function3).grid(row=2,sticky=E,padx=25,pady=25)

            #creating attendance button
            Button(self.goff,text="Attendance Sheet",font=('times new roman',30),bg="#1B58B2",fg="white",command=self.attend).grid(row=4,sticky=E,padx=25,pady=25)

            Button(self.goff,text="     classification  ",font=('times new roman',30),bg="#1B58B2",fg="white",command=self.function7).grid(row=6,sticky=W,padx=25,pady=25)

            Button(self.goff,text="   Assistance        ",font=('times new roman',30),bg="#1B58B2",fg="white",command=self.function8).grid(row=6,sticky=E,padx=25,pady=25)
            Button(self.goff,text="     performance        ",font=('times new roman',30),bg="#1B58B2",fg="white",command=self.graph).grid(row=9,sticky=N+E+S+W,padx=25,pady=25)



            Button(self.goff,text="Exit",font=('times new roman',30),bg="orange",fg="black",command=self.function6).grid(row=12,sticky=N+E+W+S,padx=30,pady=30)
            self.goff.pack()
            
        else:
             ms.showerror('Oops!','Username Not Found.')
            



if __name__ == '__main__':
	#Create Object
	#and setup window
    window = Tk()
    pyexec = sys.executable
    window.title('LOGIN Form')
    window.geometry('2080x1220')
    
    main(window)
  
    #root.mainloop()﻿
