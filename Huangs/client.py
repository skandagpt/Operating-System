import socket
import json
import _thread
import time
import random
import threading


class Error:
    commandInputError = Exception("Please enter correct command")
    portInputError = Exception("Please enter correct port number")
    controllerError = Exception("Controller Error. Try After Sometime")
    createRoomError = Exception("Error in creating the room")


class Client:
    def __init__(self, host, port,id):
        self.id=id
        self.host = host
        self.port = port
        self.connections= []
        self.weight = ""

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
            data = client.recv(1024)
            data=self.decode(data)
            message= data[:data.find('(')]
            if(message=="B"):
                self.weight = data[data.find('(')+1:data.find(')')]
                print("Assigned Weight to Process {} is: {}".format(self.id,self.weight))
                time.sleep(random.randint(1,20))
                client.send(self.encode("C({})".format(self.weight)))
        client.close()
        exit(0)
                    

    def start(self):
        client = self.createSocket(self.port)
    # _thread.start_new_thread(self.send, (client,))
        _thread.start_new_thread(self.listen, (client,))
        while True:
                continue



