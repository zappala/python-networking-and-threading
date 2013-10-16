import socket
import sys

class Server:
    """ Server that handles one client at a time. """
    def __init__(self,port):
        self.host = ""
        self.port = port
        self.size = 1024
        self.open_socket()

    def open_socket(self):
        """ Setup the socket for incoming clients """
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            self.server.bind((self.host,self.port))
            self.server.listen(5)
        except socket.error, (value,message):
            if self.server:
                self.server.close()
            print "Could not open socket: " + message
            sys.exit(1)

    def run(self):
        while True:
            (client,address) = self.server.accept()
            self.handleClient(client)

    def handleClient(self,client):
        """ Handle a client by echoing data back """
        while True:
            data = client.recv(self.size)
            if data:
                client.send(data)
            else:
                client.close()
                break
