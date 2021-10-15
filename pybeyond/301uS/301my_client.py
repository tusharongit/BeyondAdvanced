# client-server-based microservices

# a socket server can be opened to listen to requests
import socket
import sys

def myClient():

    #open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # family INET and type STREAM
    param_tup = ('localhost', 9874)
    
    #connect to server
    sock.connect(param_tup)

    # send a message to the server
    if len(sys.argv) > 1:
        # join the sys arguments with a space between them
        msg = ' '.join(sys.argv[1:])
    else:
        msg = "Default message"
    
    sock.send(msg.encode())

    # handle response from server
    res = sock.recv(1024)
    print(res)

    #clean-up
    sock.close()


if __name__ == '__main__':
    myClient()


