import socket

Host = '127.0.0.1'
port = 10016
flag = [0,0,0]
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created Successfully')
print('-----------------------------------')
my_socket.connect((Host, port))
print('Socket binded Successfully to port ',port)
# my_socket.send('Connected'.encode())

while True:
    txt = my_socket.recv(1024).decode()
    if txt[7] == '2':
        flag[1] += 1
    elif txt[7] == '3':
        flag[2] += 1
    print(txt, flag)
    
    data = input('Client 1 : ')
    if data == '':
        continue
    else:
        flag[0] += 1
        senddata = 'Client 1 : '+ data
        my_socket.send(senddata.encode())
        if data == 'close()':
            break