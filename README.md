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
