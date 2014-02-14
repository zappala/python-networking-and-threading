import os
import sys

# Run a set of download experiments

# List of URLs to download
urls = [        ("small","https://dl.dropboxusercontent.com/u/543382/design-philosophy-sigcomm-88.pdf"),
                ("medium","https://dl.dropboxusercontent.com/u/543382/Delta-Rae-Morning-Comes-Live.mp3"),
                ("large","https://dl.dropboxusercontent.com/u/543382/poster.pdf")]


# Number of threads to use
threads = [1,2,3,5,10]

# Number of times to repeat each experiment
times = 10

# Run experiment for each URL with a given number of threads
for (name,url) in urls:
    for thread in threads:
        sys.stdout.write("Running experiment for %s with %s threads" % (url,thread))
        output = "data-%s.txt" % (name)
        for i in range(0,times):
            sys.stdout.write(".")
            os.system("python downloadAccelerator.py -n %s %s >> %s" % (thread,url,output))
            sys.stdout.flush()
        print
