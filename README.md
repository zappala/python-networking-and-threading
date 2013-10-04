# Python Networking and Threading

Sample code for Python networking and threading

## Download

This small program downloads a set of URLs, located in `urls.txt`, and
stores them in a directory called `downloads`.

> python download.py

You can also supply parameters using:

> python download.py -i [input file] -d [download directory]

## Threaded Download

This program uses a separate thread to download each URL:

> python threadedDownload.py

You can also supply parameters using:

> python download.py -i [input file] -d [download directory]
