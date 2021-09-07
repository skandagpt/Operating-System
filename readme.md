# Advanced Operating System
 - [Server-Client Model](#server-client-model)
   - [Chatroom](#chatroom)
     - [Controller](#controller)
     - [Server](#server)
     - [Client](#client)
   - [How to run](#how-to-run)
   - [Commands](#commands)
     - [Create Chatroom](#create-chatroom)
     - [Join Chatroom](#join-chatroom)
     - [List all members](#list-all-members)
       [Leave the chatroom](#leave-the-chatroom)

## Server-Client Model
Server-Client application using socket programming
### Chatroom
Clients can create different chatrooms and chat among themselves
#### Controller
Used to create and join chatrooms
#### Server
Medium for the chatroom.Every chatroom has its own server
#### Client
Users can create and join different chatrooms

### How to run
Run controller on one terminal

    python3 controller.py

Run clients on different terminal

    python3 client.py


### Commands
#### Create Chatroom
    ./createRoom
#### Join Chatroom
    ./join
You'll be asked the port number of the chatroom you want to join.

After joining the chatroom
#### List all members
    ./members
#### Leave the chatroom
    ./leave
