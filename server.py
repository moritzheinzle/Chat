import socket 
import select 
import sys 
from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
 
if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address, port number")
    exit()  
IP_address = str(sys.argv[1])  
Port = int(sys.argv[2]) 
server.bind((IP_address, Port)) 
server.listen(100) 
list_of_clients = [] 

