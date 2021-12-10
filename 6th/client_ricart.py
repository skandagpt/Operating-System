import socket
import json
import _thread
import time
import threading


class Error:
    commandInputError = Exception("Please enter correct command")
    portInputError = Exception("Please enter correct port number")
    controllerError = Exception("Controller Error. Try After Sometime")
    createRoomError = Exception("Error in creating the room")


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.flag = 0

    def createSocket(self, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        client.connect((self.host, port))
        return client

    def decode(self, value):
        return value.decode('ascii')

    def encode(self, value):
        return value.encode('ascii')
    
    def listen(self,client):   
        while True:
            try:
                data = client.recv(1024)
                if not data:
                    break
                print(self.decode(data))
            except :
                continue
        client.close()
        exit(0)

    def listen_10(self, client):
        client.settimeout(0.1)
        vr=False
        for i in range(100):
            try:
                data = client.recv(1024)
                if(self.decode(data) == "REPLY"):
                    print("Reqeust Granted")
                    vr=True
                    exit(0)
            except:
                continue
        if(vr==False):
            print("Request Denied")
            exit(0)
        

    def send(self, client):
        while True:
            try:
                message = input("")
                if(message == "REQUEST"):
                    timestamp= time.time()
                    message = message + "~" + str(int(timestamp))
                    _thread.start_new_thread(self.listen_10, (client,))
                else:
                    message = message + "~"
            except Exception as e:
                continue
            client.send(self.encode(message ))
            

    def start(self):
        client = self.createSocket(self.port)
        name = input("Enter Name : ")
        client.send(name.encode('ascii'))

        _thread.start_new_thread(self.send, (client,))
        # _thread.start_new_thread(self.listen, (client,))
        while True:
                continue


if __name__ == '__main__':
    client = Client('127.0.0.1', 1236)
    client.start()
