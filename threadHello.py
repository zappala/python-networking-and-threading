import argparse
import sys
import threading

class Hello(threading.Thread):
    """ A thread that says hello. """
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print "Hello from thread",self.getName()



def parse_options():
        parser = argparse.ArgumentParser(prog='threadHello', description='Simple demonstration of threading', add_help=True)
        parser.add_argument('-n', '--number', type=int, action='store', help='Specify the number of threads to create',default=10)
        return parser.parse_args()

if __name__ == "__main__":
    args = parse_options()
    threads = []
    for i in range(0,args.number):
        h = Hello()
        threads.append(h)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

