import optparse
import sys

import matplotlib
matplotlib.use('Agg')
from pylab import *

# Class that parses a file and plots several graphs
class Plotter:
    def __init__(self):
        pass

    def parse(self,filename):
        """ Parse the data file and accumulate values for plots. 
        """
        # Initialize plotter variables.
        self.data = {}
        self.sizes = {}
		# open file
        f = open(filename)
        for line in f.readlines():
			# skip lines starting with a comment character
            if line.startswith("#"):
                continue
			# try parsing the line
            try:
                url,threads,size,seconds = line.split()
            except:
                continue
			# convert to proper data types
            threads = int(threads)
            size = int(size)
            seconds = float(seconds)
			# add to dictionary
            if threads not in self.data:
                self.data[threads] = []
            self.data[threads].append(seconds)

    def plot(self,name):
		clf()
		# plot download times
		x = []
		keys = []
		# collect data into a list of lists
		for threads in sorted(self.data.keys()):
			x.append(self.data[threads])
			keys.append(threads)
		# plot all the lists as a boxplot
		boxplot(x,positions=keys)
		xlabel('Number of Threads')
		ylabel('Download Time')
		savefig('download-time-%s.pdf' % name)

if __name__ == '__main__':
    p = Plotter()
    p.parse('data-small.txt')
    p.plot('small')
    p.parse('data-medium.txt')
    p.plot('medium')
    p.parse('data-large.txt')
    p.plot('large')
