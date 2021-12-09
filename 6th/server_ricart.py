import socket as socket
import _thread
import threading


class Server:

    def __init__(self,port,host="",):
        self.host =host
        self.port= port
        self.connection = []
        self.allocated=""
        self.timestamp=0
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def configure(self):
        try:
            self.server.bind((self.host, self.port))
            print("Server binded to port", self.port)
            self.server.listen(5)
            print("Server is listening")
        except  Exception as e:
            print(e)

    def decode(self, value):
        return value.decode('ascii')

    def encode(self, value):
        return value.encode('ascii')

    def broadcast(self, client, message):
        for x in self.connection:
            if x != client:
                x.send(self.encode(message))

    def threaded(self, client, client_addr,client_name):
        while True:
            try:
                data = client.recv(1024)
                if not data or str(self.decode(data))=="./leave":
                    self.connection.remove(client)
                    break
                data=str(self.decode(data))
                command = data[0:data.find("~")]
                if command=="REQUEST" :
                    if self.allocated=="":
                        self.allocated=client_name
                        self.timestamp=int(data[data.find("~")+1:])
                        client.send(self.encode("REPLY"))
                    else:
                        print("Timestamp of {} is {}".format(client_name,int(data[data.find("~")+1:])))
                        print("Timestamp of {} is {}".format(self.allocated,self.timestamp))
                        print("Resource cannot be allocated to {}".format(client_name))

                if command=="REPLY":
                    if self.allocated==client_name:
                        self.allocated=""
                        self.timestamp=0
                        self.broadcast(client, "REPLY")
                        print("Resource is released")
                    


            except  Exception as e:
                print(e)
                break
        client.close()

    def start(self):
        self.configure()
        while True:
            client, client_addr = self.server.accept()
            client_name = client.recv(1024)
            self.connection.append(client)
            print('Connected to :', client_addr[0], ':', client_addr[1])

            _thread.start_new_thread(
                self.threaded, (client,client_addr ,client_name.decode('ascii')))

if __name__ == '__main__':
    server=Server(1235);
    server.start()
