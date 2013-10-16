# Python Networking and Threading

Sample code for Python networking and threading

## Simple Threading Examples

In the `threading` directory are two programs to demonstrate the use
of threading in Python. The program `threadHello.py` shows how to
create a set of threads that print a message and their thread ID.

> python threadHello.py -n [number]

The program `threadShared.py` shows how to use shared memory with
threads.  Each thread has a shared variable i that is NOT protected
with semaphores, and another one that is properly protected and
accessed through a thread-safe object.

> python threadShared.py -n [number]

## Download

In the `download` directory are two programs that demonstrate using
the Python Requests library. The program `download.py` downloads a set
of URLs, located in `urls.txt`, and stores them in a directory called
`downloads`.

> python download.py -i [input file] -d [download directory]

The program `threadedDownload.py` creates a separate thread to
download each URL in parallel:

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

## Echo Server

The code in the `echo-server` directory shows how to use the
lower-level Python sockets library as well as how to create a server
based on polling. The program `echo-server.py` uses `server.py` to create
a basic echo server:

> python echoserver.py -p [port]

The program `echo-client.py` uses `client.py` to create a basic echo client:

> python echoclient.py -s [server] -p [port]

This version of the echo server can handle only one client at a time.

The program `echoserver-poll.py` uses `poller.py` to show how a server
can use the poll() system call to multiplex handling multiple clients
while using a single thread of control.

Note that because the server is so simple, this code does not do many
other things a polling server should do, such as using non-blocking
I/O, timing out idle sockets, and using a separate receive cache for
each client.
