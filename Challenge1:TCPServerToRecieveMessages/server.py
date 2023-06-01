"""
This is the server side code for the server to just recieve messages. 
The server gets initialized and then creates a thread for each new client.
"""
import socket
from _thread import *

address = "localhost"
port = 8080

#Initialize socket
TCPsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to address and port
TCPsocket.bind((address, port))
print(f"Server up on address {address} and port {port}")

#Socket starts listening to incoming connections
TCPsocket.listen(10)

#Individual thread for each client, simple while loop that listens for incoming
#messages
def clientthread(connection, address):
    while True:
        msg = (connection.recv(2048))
        connection.sendall(msg)
        msg = msg.decode("utf-8")
        print(f"{address}: {str(msg)}")

#While loop that listens for new connections and creates thread for them
while True:
    connection, address = TCPsocket.accept()
    print(f"{address} joined the server")
    start_new_thread(clientthread, (connection, address))
