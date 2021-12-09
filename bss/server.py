import socket 
import threading
import sys
import bss
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind(('',5008))
flag = [1,1,1]
IP = ['10.0.0.1','10.0.0.2','10.0.0.3']
d = { '10.0.0.2' : "giri" , '10.0.0.3' : "harsi"}

def receiver(threadname,x):
	global sock
	while True:
		data , add = sock.recvfrom(1024)
		if not bss.check(data, add, flag):
			break
	sock.close()	

bss.initialise(3,0)

UDP_PORT = 5008
thread = threading.Thread(target = receiver , args = ("Receive" ,0 ))
thread.start()
print("Enter data to be sent. Enter \"exit\" to exit")
message=input()

while message!="exit":
	bss.update()
	message = message.replace(" " ,"~")
	message += " "
	for i in bss.timestamp:
		message += str(i) + ","
	message += " " + str(bss.my_index)
	print(message)
	for i in range(len(flag)):
		if i != bss.my_index and flag[i] == 1:
			sock.sendto(message.encode(),(IP[i],UDP_PORT))
	message = input("Enter data to be sent. Enter \"exit\" to exit : ")
    
message += " "
print("Exiting")
bss.update()
for i in bss.timestamp:
	message += str(i) + ","
message += " " + str(bss.my_index)
print(message)
for i in range(len(flag)):
	if i!=bss.my_index and flag[i]:
		sock.sendto(message.encode(),(IP[i],UDP_PORT))	
sock.close()

print("system exit")
sys.exit(0)