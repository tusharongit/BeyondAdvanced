# client-server-based microservices

# a socket server can be opened to listen to requests
import socket

def myServer():

    #open socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # family INET and type STREAM

    # configure the socket
    param_tup = ('localhost', 9874)
    server.bind(param_tup)

    # begin listening for requests
    server.listen(5) # we can configure the max no. of connections
    print('The server is listening on {} port {}'.format(param_tup[0], param_tup[1]))

    # respond to requests in an endless loop, with a quit option
    while True:
        # unpack the request
        (client, addr) = server.accept()
        # read data from client
        buf = client.recv(1024) # read the first 1024
        print('Server received {}'.format(buf))
        # send a response back to the client
        client.send(buf.upper())
        # need to quit and close the server
        if buf == b'quit':
            print('server closing')
            server.close()
            break # breaks out of the while loop


if __name__ == '__main__':
    myServer()