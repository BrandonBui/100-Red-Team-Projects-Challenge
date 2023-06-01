"""
Client side code.  Initializes the client socket and connects to the server.
Loop of read in message, send message to server, and recieves echoed message.
"""
import socket
import select
import sys
from _thread import *

address = "localhost"
port = 8080

#Initializes socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connects to the server
server.connect((address, port))
print(f"Connected to {address} on port {port}")
#Reads in message and sends to server
while True:
    message  = sys.stdin.readline()
    server.sendall(bytes(message, "utf-8"))
    sys.stdout.flush()
    print("You: " + str((server.recv(2048).decode("utf-8"))))
server.close()