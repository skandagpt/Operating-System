
timestamp = []
my_index = 0
mess_queue = []

def message_ordered(data):
	f = 1
	timestamp2 = data[1].split(',')
	if int(timestamp2[int(data[2])])!=timestamp[int(data[2])]+1:
		f = 0
	for i in range(len(timestamp)):
		if i !=int(data[2]):
			if timestamp[i] < int(timestamp2[i]):
				f = 0
	return f

def initialise(n,x):
	global timestamp
	global my_index
	timestamp = [0]*n
	my_index = x


def update():
	timestamp[my_index] += 1

def display_message(data):
	print(data.replace("~"," "))

def check(data, add,flag):
	data = data.split()
	if data[0] == 'exit':
		flag[int(data[2])] = 0
	if message_ordered(data):
		timestamp[int(data[2])] += 1
		display_message(data[0])
		f = 1
		while f:
			f = 0
			for i in mess_queue:
				if message_ordered(i):
					timestamp[int(i[2])] += 1
					display_message(i[0])
					del mess_queue[mess_queue.index(i)]
					f = 1
	else:
		print ("Queued message")
		mess_queue.append(data)

	if all(v == 0 for v in flag):
		return 0
	return 1