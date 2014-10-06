import os
import sys

# Run a set of download experiments

# List of URLs to download (Census Bureau)

urls = [        ("small","http://www2.census.gov/geo/tiger/TIGER2013/TRACT/tl_2013_10_tract.zip"),
                ("medium","http://www2.census.gov/geo/tiger/TIGER2013/EDGES/tl_2013_35005_edges.zip"),
                ("large","http://www2.census.gov/geo/tiger/TGRGDB13/tlgdb_2013_a_39_oh.gdb.zip")]

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
