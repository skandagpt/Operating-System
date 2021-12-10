import socket
from server import Server
import _thread
import threading
import json

class Controller:
    def __init__(self,port,host=''):
        self.port=port
        self.host=host
        self.controller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.configure()

    def configure(self):
        self.controller.bind((self.host, self.port))
        print("Server binded to port", self.port)
        self.controller.listen(5)
        print("Server is listening")

    def decode(self, value):
            return value.decode('ascii')

    def encode(self, value):
        return value.encode('ascii')

    def threaded(self,admin,port):
        try:
            server = Server(port=port,admin=admin)
            server.configure()
            server.start()
        except  Exception as e:
            print("Thread exception",e)
            self.port+=1
            self.threaded(admin,self.port)

    def listen(self):
        self.count = self.port + 1 
        while True:
            client, client_addr = self.controller.accept()
            command = client.recv(1024)
            if self.decode(command)=="./createRoom":
                _thread.start_new_thread(self.threaded,(client_addr,self.count))
                result = {
                    "status":200,
                    "port":self.count,
                    "type":"creation",
                    "message":"CHATROOM CREATED"}
                client.send(self.encode(json.dumps(obj=result)))
                self.count+=1
                
                
if __name__ == '__main__':
    controller = Controller(12343)
    controller.listen()