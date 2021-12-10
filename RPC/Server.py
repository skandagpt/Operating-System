import socket

def add(x,y):
    return x + y

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
conn.send('Successfully Connected to Client'.encode())
    
while True:        
    data = conn.recv(1024).decode()
    print('Client :',data)
    if data == 'close()':
        my_socket.close()
        break
    if data[0:4] == 'add(':
        x, y = '', ''
        i = 4
        while data[i] != ',':
            x += data[i]
            i += 1
        y += data[i+1:-2]
        xint= int(x)
        yint = int(y)
        txt = str(add(xint,yint))
        print('Server: ',txt)
    else:
        txt = input('Server: ')
    conn.send(txt.encode())
    


