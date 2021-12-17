import socket
import os
import threading 
from threading import Thread
socket.setdefaulttimeout(100)
clients = set()
clients_lock = threading.Lock()

def listener(client, address):
    print("Accepted connection from: ", address)
    client.send('Connected'.encode())
    with clients_lock:
        clients.add(client)
    try:    
        while True:
            data = client.recv(1024)
            if not data:
                break
            else:
                print (data.decode())
                with clients_lock:
                    for c in clients:
                        c.sendall(data)
    finally:
        with clients_lock:
            clients.remove(client)
            client.close()
    client.close()

host = '127.0.0.1'
port = 10016

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(3)
th = []

while True:
    print ("Server is listening for connections...")
    client, address = s.accept()
    th.append(Thread(target=listener, args = (client,address)).start())
    if not socket.timeout :
        break
s.close()