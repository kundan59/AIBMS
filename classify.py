import sqlite3
import requests
import os



c=[]
m=[]
s=[]
conn=sqlite3.connect("Face.db")
cmd="SELECT id,marks,attendance FROM  report where marks<=55"
cursor=conn.execute(cmd)
for row in cursor:
    if row[2]<65:
        c.append(row[0])
conn.close()



conn=sqlite3.connect("Face.db")
cmd="SELECT id,marks,attendance FROM  report where marks between 56 and 74"
cursor=conn.execute(cmd)
for row in cursor:
    if row[2]<65:
        m.append(row[0])
conn.close()


conn=sqlite3.connect("Face.db")
cmd="SELECT id,marks,attendance FROM  report where marks >= 75"
cursor=conn.execute(cmd)
for row in cursor:
    if row[2]>65:
        s.append(row[0])

conn.close()
print("        AVERAGE_STUDENTS        ",end="\n")
print("ID",end=' ')
print("NAME",end='              ')
print("MARKS",end='  ')
print("ATTENDANCE",end='\n')
print("......................................................",end="\n")
for i in range(0,len(c)):
    conn=sqlite3.connect("Face.db")
    cmd="SELECT id,name,marks,attendance FROM  report where id="+str(c[i])
    cursor=conn.execute(cmd)
    
    
    for row in cursor:
        print(row[0],end='  ')
        print(row[1],end='  ')
        print(row[2],"%",end='  ')
        print(row[3],"%",end='\n')
print("---------------------------------------------------------------")
print("\n")

print("        GOOD_STUDENTS        ",end="\n")
print("ID",end=' ')
print("NAME",end='              ')
print("MARKS",end='  ')
print("ATTENDANCE",end='\n')
print("......................................................",end="\n")
for i in range(0,len(m)):
    conn=sqlite3.connect("Face.db")
    cmd="SELECT id,name,marks,attendance FROM  report where id="+str(m[i])
    cursor=conn.execute(cmd)
    
    
    for row in cursor:
        print(row[0],end='  ')
        print(row[1],end='  ')
        print(row[2],"%",end='  ')
        print(row[3],"%",end='\n')
print("---------------------------------------------------------------")
print("\n")
print("        EXCELLENT_STUDENTS        ",end="\n")
print("ID",end=' ')
print("NAME",end='              ')
print("MARKS",end='  ')
print("ATTENDANCE",end='\n')
print("......................................................",end="\n")
for i in range(0,len(s)):
    conn=sqlite3.connect("Face.db")
    cmd="SELECT id,name,marks,attendance FROM  report where id="+str(s[i])
    cursor=conn.execute(cmd)
    
    
    for row in cursor:
        print(row[0],end='  ')
        print(row[1],end='  ')
        print(row[2],"%",end='  ')
        print(row[3],"%",end='\n')
input("press enter to exit")   

               
               

        



