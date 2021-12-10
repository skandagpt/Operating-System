
import sys
import threading
import time
from random import randint


no_threads = 5
no_requests = 5

print ("Threads =", no_threads)
print ("Requests =", no_requests)


###################################### Distributing requests across threads #####################################
distribution = []
no = 0
for itr in range(0, no_threads):
	distribution.append(0)
for itr in range(0, no_requests):
    	# print ("assign request %d to thread %d" % (itr, no))
    	distribution[no] += 1
    	no = (no + 1) % no_threads

#for itr in range(0, no_threads):
#    	print ("distribution[%d] = %d" % (itr, distribution[itr]))


###################################### Lamport's fast mutual exclusion algorithm #################################

requestno = 0
y = -1
x = -1
b = []
for itr in range(0, no_threads):
	b.append(0)

def thread_lamport_fast(threadno):
	global distribution
	global requestno
	global no_requests
	global no_threads
	global y
	global x
	global b
	reqs = distribution[threadno]
	# print ("starting thread", threadno)
	time.sleep(1)
	
	while reqs:

		########## requesting CS ######
		print (threadno, "Requesting CS")
		b[threadno] = 1                                                # Indicates contending
		x = threadno
		if y != -1:                                                    # Shows there is contention
			b[threadno] = 0
			# print ("\tthread", threadno, "Waiting until CS is released")
			while (y != -1):
				pass
			continue
		y = threadno

		if x != threadno:                                              # Shows there is contention
			b[threadno] = 0
			for j in range(0, no_threads):                         # Awaits for other contending processes to finish
				while ( b[j] != 0 ):
					pass
			# print ("\tthread", threadno, "Checking the barrier")
			if y != threadno:
				while (y != -1):
					pass
				continue

		########## entering CS ########
		requestno = requestno + 1
		print (threadno, "Entering CS")
		reqs = reqs - 1
		# time.sleep(randint(1,2))                                     # uncomment for better distribution of requests

		########## exiting CS #########
		print (threadno, "Exiting CS")
		y = -1
		b[threadno] = 0                                                # Exiting critical section

		###############################
		# time.sleep(randint(1,2))                                     # uncomment for better distribution of requests

		
print ("Running Lamport's fast mutual exclusion algorithm:")
for threadno in range(0, no_threads):
	th = threading.Thread(target=thread_lamport_fast, args=(threadno,))
	th.daemon = True
	th.start()

while (requestno < no_requests):
	pass
time.sleep(1)
print ("Finishing Lamport's fast mutual exclusion. All requests served. requestno =", requestno, "\n\n")
time.sleep(5)


###################################### Lamport's bakery algorithm ################################################

requestno = 0
choosing = []
num = []
for itr in range(0, no_threads):
	choosing.append(0)
	num.append(0)

def thread_lamport_bakery(threadno):
	global requestno
	global no_requests
	global no_threads
	global choosing
	global num
	reqs = distribution[threadno]
	# print ("starting thread", threadno)
	time.sleep(1)

	while reqs:

		########## requesting CS ######
		print (threadno, "Requesting CS")
		choosing[threadno] = 1		# Maintains request counter
		num[threadno] = 1 + max(num)	# Assigns the next token number
		print (threadno , "Received Token", num[threadno] )
		choosing[threadno] = 0
		for j in range(0, no_threads):
			while(choosing[j] != 0): # Wait if the process is currently choosing
				pass
			while((num[j] !=0) & ((num[j] < num[threadno]) | ((num[j] == num[threadno]) & (j < threadno)))):
				pass

		########## entering CS ########
		requestno = requestno + 1
		print (threadno, "Entering CS")
		reqs = reqs - 1
		# time.sleep(randint(1,2))                                     # uncomment for better distribution of requests

		########## exiting CS #########
		print (threadno, "Exiting CS")
		num[threadno] = 0

		###############################
		# time.sleep(randint(1,2))                                     # uncomment for better distribution of requests


print ("Running Lamport's bakery algorithm:")
for threadno in range(0, no_threads):
	th = threading.Thread(target=thread_lamport_bakery, args=(threadno,))
	th.daemon = True
	th.start()

while (requestno < no_requests):
    	pass
time.sleep(1)
print ("Finishing Lamport's bakery algorithm. All requests served. requestno =", requestno, "\n\n")
time.sleep(1)

