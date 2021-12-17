import socket

Host = '127.0.0.1'
port = 5786

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created Successfully')
print('-----------------------------------')
my_socket.bind((Host, port))
print('Socket binded Successfully to port ',port)

my_socket.listen()
print('Server is listening')

conn, addr = my_socket.accept()
print('Connected to ', addr)
conn.send('Enter the file name: '.encode())
data = conn.recv(1024).decode()
print('Client :',data)
file1 = open(data,"r")
while True:
    lines = file1.readline(1024)
    conn.send(lines.encode())
    print(lines)
    if lines == '':
        break
file1.close()
# txt = input('Server: ')

my_socket.close()




