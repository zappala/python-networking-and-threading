import argparse
import sys
import threading

class Shared:
    """ Shared memory """
    def __init__(self):
        self.i = 0
        self.sem = threading.Semaphore()
        self.lock = threading.Lock()

    def inc(self):
        """ increment the shared varable """
        self.sem.acquire()
        self.i = self.i + 1
        s = self.i
        self.sem.release()
        return s

class Hello(threading.Thread):
    """ A thread that increments and prints both a local and shared
    variable """
    def __init__(self,shared):
        threading.Thread.__init__(self)
        self.i = 0
        self.shared = shared

    def run(self):
        self.i = self.i + 1
        s = self.shared.inc()
        with self.shared.lock:
            print "Hello from thread %s i = %d shared = %d" % (self.getName(),self.i,s)

def parse_options():
        parser = argparse.ArgumentParser(prog='threadHello', description='Simple demonstration of threading', add_help=True)
        parser.add_argument('-n', '--number', type=int, action='store', help='Specify the number of threads to create',default=10)
        return parser.parse_args()

if __name__ == "__main__":
    args = parse_options()
    s = Shared()
    for i in range(0,args.number):
        h = Hello(s)
        h.start()
