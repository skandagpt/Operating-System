import socket

Host = '127.0.0.1'
port = 5786

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created Successfully')
print('-----------------------------------')
my_socket.connect((Host, port))
print('Socket binded Successfully to port ',port)
my_socket.send('Connected'.encode())
print(my_socket.recv(1024).decode())

while True:
    
    txt = my_socket.recv(1024).decode()
    print('Server :',txt)
    data = input('Client : ')
    my_socket.send(data.encode())
    if data == 'close()':
        break