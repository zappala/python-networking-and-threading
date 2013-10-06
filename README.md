# Python Networking and Threading

Sample code for Python networking and threading

## Download

This small program downloads a set of URLs, located in `urls.txt`, and
stores them in a directory called `downloads`.

> python download.py -i [input file] -d [download directory]

## Simple Threading Examples

The program `threadHello.py` shows how to create a set of threads that
print a message and their thread ID.

> python threadHello.py -n [number]

The program `threadShared.py` shows how to use shared memory with
threads.  Each thread has a shared variable i that is NOT protected
with semaphores, and another one that is properly protected and
accessed through a thread-safe object.

> python threadShared.py -n [number]

## Threaded Download

This program modifies `download.py` to create a separate thread to
download each URL:

> python download.py -i [input file] -d [download directory]

## Download Accelerator Experiments

The code in the `download-accelerator` directory is for a lab
[download
accelerator](http://cs360.byu.edu/fall-2013/labs/download-accelerator)
where students write a script that downloads a file in parallel.  The
file `experiments.py` calls the `downloadAccelerator.py` script to
download files of several different sizes using a variable number of
threads.

> python experiments.py

The file `plot.py` uses the data collected with the experiments to
create a series of boxplots showing the distribution of the download
time versus the number of threads, one for each file.

> python plot.py


