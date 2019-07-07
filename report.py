import sqlite3
import requests
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

for i in range(0,len(c)):
    conn=sqlite3.connect("Face.db")
    cmd="SELECT mnumber from peoples where id="+str(c[i])
    cursor=conn.execute(cmd)
    for row in cursor:
        url = "https://www.fast2sms.com/dev/bulk"
 
        payload = "sender_id=FSTSMS & message=Dear student your performance is below average in the examination and your attendance is also less than 65 so, please attend your all respective lectures and improve your marks.    & language=english & route=p & numbers="+str(row[0])
        headers = {
         'authorization': "zg6YJqFs2wCbPGM9H5p4QOiDlSAca7KvIhWrLxNmEX0RoVBdkefWOGmNVHeR9d6lM8Kzn07gQPBhusFU",
         'Content-Type': "application/x-www-form-urlencoded",
         'Cache-Control': "no-cache",
         }
 
        response = requests.request("POST", url, data=payload, headers=headers)
 
        print(response.text)


conn=sqlite3.connect("Face.db")
cmd="SELECT id,marks,attendance FROM  report where marks between 56 and 75"
cursor=conn.execute(cmd)
for row in cursor:
    if row[2]<65:
        m.append(row[0])
conn.close()

for i in range(0,len(m)):
    conn=sqlite3.connect("Face.db")
    cmd="SELECT mnumber from peoples where id="+str(m[i])
    cursor=conn.execute(cmd)
    for row in cursor:
        url = "https://www.fast2sms.com/dev/bulk"
 
        payload = "sender_id=FSTSMS & message=Dear student your performance is  good in the examination and but your attendance is less than 65 so, please attend your all respective lectures so you will get excellent marks.    & language=english & route=p & numbers="+str(row[0])
        headers = {
         'authorization': "zg6YJqFs2wCbPGM9H5p4QOiDlSAca7KvIhWrLxNmEX0RoVBdkefWOGmNVHeR9d6lM8Kzn07gQPBhusFU",
         'Content-Type': "application/x-www-form-urlencoded",
         'Cache-Control': "no-cache",
         }
 
        response = requests.request("POST", url, data=payload, headers=headers)
 
        print(response.text)

conn=sqlite3.connect("Face.db")
cmd="SELECT id,marks,attendance FROM  report where marks between 56 and 75"
cursor=conn.execute(cmd)
for row in cursor:
    if row[2]<65:
        s.append(row[0])
conn.close()
print(s)
for i in range(0,len(s)):
    conn=sqlite3.connect("Face.db")
    cmd="SELECT mnumber from peoples where id="+str(s[i])
    cursor=conn.execute(cmd)
    for row in cursor:
        url = "https://www.fast2sms.com/dev/bulk"
 
        payload = "sender_id=FSTSMS & message=Dear student your performance is excellent in the examination and but your attendance is less than 65 so, please attend your all respective lectures so that your consistancy will be maintain    & language=english & route=p & numbers="+str(row[0])
        headers = {
         'authorization': "zg6YJqFs2wCbPGM9H5p4QOiDlSAca7KvIhWrLxNmEX0RoVBdkefWOGmNVHeR9d6lM8Kzn07gQPBhusFU",
         'Content-Type': "application/x-www-form-urlencoded",
         'Cache-Control': "no-cache",
         }
 
        response = requests.request("POST", url, data=payload, headers=headers)
 
        print(response.text)
        
               
               

        



