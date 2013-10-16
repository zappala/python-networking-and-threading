"""
A TCP echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

import argparse

from client import Client

class Main:
    """ Parse command line options and perform the download. """
    def __init__(self):
        self.parse_arguments()

    def parse_arguments(self):
        ''' parse arguments, which include '-p' for port '''
        parser = argparse.ArgumentParser(prog='Echo Server', description='A simple echo server that handles one client at a time', add_help=True)
        parser.add_argument('-s', '--server', type=str, action='store', help='host the server is running on',default='localhost')
        parser.add_argument('-p', '--port', type=int, action='store', help='port the server is bound to',default=3000)
        self.args = parser.parse_args()

    def run(self):
        c = Client(self.args.server,self.args.port)
        c.run()

if __name__ == "__main__":
    m = Main()
    m.parse_arguments()
    m.run()
