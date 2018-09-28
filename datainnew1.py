import serial 
import MySQLdb
from datetime import datetime
import time
from random import randint
###TO UPLOAD OK
# VISHNU P.R.


dbConn=MySQLdb.connect(user="root",passwd="",db="project2",unix_socket="/opt/lampp/var/mysql/mysql.sock")


'''
device = serial.Serial("/dev/ttyACM0", 9600)#this will have to be changed to the serial port you are using
 
arduino =device 
device.flushInput()
data = arduino.readline()
data = arduino.readline()
data = arduino.readline()
i=0
time.sleep(1)
device.flushInput()

i=0
'''
while True: 
  time.sleep(1)
  cursor = dbConn.cursor()
  #######data = arduino.readline()  #read the data from the arduino$$$$$$$$ REMOVE c
  #data=".86	0.0"#comment it
  print datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  p1=[0,0,0]
  p1[0]="0"
  p1[1]="0"
  p1[2]="0"
  data=".86 0.0"
  p1 =(data.split(" ") ) #split the data 
  
  
  p1[0]=randint(0, 90)
  print p1[0]
  print p1[1]
 ### print p1[2]
 

  try:

    date1 = datetime.now()
    date2 = datetime(2018,05,4) 
    if date1<date2:
   # time.sleep(1)
     
     cursor.execute("INSERT INTO `data2`(`block`, `power`, `current`,`date_in`) VALUES (%s,%s,%s,%s)",("1",p1[0],p1[1],datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

     dbConn.commit() #commit the insert
     cursor.close()  #close the cursor
     print "accepted"
     time.sleep(1) 
  except MySQLdb.IntegrityError:
    print "failed to insert data"
  finally:
   
    print ""




