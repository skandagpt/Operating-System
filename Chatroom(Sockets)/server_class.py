import socket as socket
import _thread
import threading


class Server:

    def __init__(self,port,admin,host="",):
        self.admin = admin
        self.host =host
        self.port= port
        self.connection = []
        self.members = []
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
        intial_message = "{} joined the chatroom".format(client_name)
        self.broadcast(client, intial_message)
        while True:
            try:
                data = client.recv(1024)
                
                if not data or str(self.decode(data))=="./leave":
                    self.broadcast(client, "{} left the chatroom".format(client_name))
                    self.members.remove(client_name)
                    self.connection.remove(client)
                    break
                data=str(self.decode(data))
                if data=="./members" :
                    client.send(self.encode(str(self.members)))
                    continue
                # Doesn't work as of now
                # if data.find("./kick")>=0:
                #     print(client_addr,self.admin)
                #     if(client_addr==self.admin):
                #         index = str(self.decode(data)).find(":")
                #         name = data[index+1:]
                #         print(name)
                #         try:
                #             self.connection[self.members.find(name)].close()
                #             del self.connection[self.members.find(name)]
                #             continue
                #         except :
                #             client.send(self.encode("No such user exists"))
                #             continue

                #     else:
                #         client.send(self.encode("You are not authorized to use this command"))
                #         continue

                message = "{} : {}".format(client_name, data)
                self.broadcast(client, message)
            except  Exception as e:
                print(e)
                break
        client.close()

    def start(self):
        while True:
            client, client_addr = self.server.accept()
            client_name = client.recv(1024)
            self.connection.append(client)
            self.members.append(self.decode(client_name))
            print('Connected to :', client_addr[0], ':', client_addr[1])

            _thread.start_new_thread(
                self.threaded, (client,client_addr ,client_name.decode('ascii')))


