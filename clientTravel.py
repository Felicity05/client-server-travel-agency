'''
Client program for for the Travel Agency Happy Travel
@author: Arelys Alvarez
'''

from socket import *
import sys
import time


CLIENT_BUFFER = 4096 #size of the buffer for the replay

try:
    sock = socket(AF_INET, SOCK_STREAM) #for TCP connections
except socket.error:
    print("Failed to connect")
    sys.exit()
#socket has been created

#server info
host = ''
port = 10000

ip = ''

if len(sys.argv) > 1: #get command line arguments
    ip = sys.argv[1]

try:
    ip = gethostbyname(host) #get the ip address of the host
except gaierror:
    print("Hostname could not be resolved")
    sys.exit()

# print("\nIP Address:sea " + ip)
#connect the client to the server
sock.connect((ip, port)) #server ip

#greets the client to the agency
with open("Airplane.txt") as f:
    for line in f:
        if ("#" not in line):
            print(line.strip('\n')) #to eliminate the spaces between lines when printing

print("Please type your request. \nType \"Help\" for a list of available options.\n")

#gets all the user input and send it to the server to be processed
while True:

    client_request = input('->')

    if not client_request:
        print("You need to enter something...\n")
    else:

        sock.send(str(client_request).encode('utf-8')) #encode the message to send to the server
        server_answer = sock.recv(CLIENT_BUFFER).decode('utf-8') #save and decode the message sent by the server

        # disconnects the client
        if(client_request == "bye" or client_request == "quit" or client_request == 'exit'):
            sock.send("disconnect".encode()) #send key word to notify the server that the client has been disconnected
            print("Thanks for traveling with us. Have a wonderful day! Bye bye")
            sock.close() # to properly close the socket in the client side
            sys.exit()

        if not server_answer:
            print("No answer from server. It may be disconnected\n")
            break

        #print the server answer
        print(server_answer)


#outside the loop once the connection is finished
print("\n Socket connected to: \""+ host + "\" using ip: "+ ip)

sock.close()


