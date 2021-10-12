# depending on user input from the client, either call the weather uS or the typicode uS
# 'stage' is the client which calls on the 'serve' server which calls the corresponding uS

# a socket server can be opened to listen to requests
import socket
import sys
import uS_typicode
import uS_weather

def myServer():

    #open socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # family INET and type STREAM

    # configure the socket
    param_tup = ('localhost', 9874)
    server.bind(param_tup)

    # begin listening for requests
    server.listen(5) # we can configure the max no. of connections
    # print('The server is listening on {} port {}'.format(param_tup[0], param_tup[1]))

    # respond to requests in an endless loop, with a quit option
    response=''
    while True:
        # unpack the request
        (client, addr) = server.accept()
        # read data from client
        buf = client.recv(1024) # read the first 1024
        print('Server received {}'.format(buf))
        # send a response back to the client
        buf = buf.decode()
        buf_list = buf.split(' ')
        if buf_list[0] == 'weather':
            response=uS_weather.reportWeather(buf_list)
        elif buf_list[0] == 'typicode':
            response=uS_typicode.getInfo(buf_list)
        else:
            response='Expecting weather or typicode after filename'


        client.send(response.encode())
        
        # need to quit and close the server
        if buf == b'quit':
            print('server closing')
            server.close()
            break # breaks out of the while loop


if __name__ == '__main__':
    myServer()