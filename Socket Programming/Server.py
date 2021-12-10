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
conn.send('Successfully Connected to Server'.encode())
    
while True:        
    data = conn.recv(1024).decode()
    print('Client :',data)
    if data == 'close()':
        my_socket.close()
        break
    txt = input('Server: ')
    conn.send(txt.encode())
    


