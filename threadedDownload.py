import argparse
import os
import requests
import threading

''' Downloader for a set of files '''
class Downloader:
    def __init__(self):
        ''' initialize the file where the list of URLs is listed, and the
        directory where the downloads will be stored'''
        self.args = None
        self.in_file = 'urls.txt'
        self.dir = 'downloads'
        self.parse_arguments()

    def parse_arguments(self):
        ''' parse arguments, which include '-i' for input file and
        '-d' for download directory'''
        parser = argparse.ArgumentParser(prog='Mass downloader', description='A simple script that downloads multiple files from URLs specified in a file', add_help=True)
        parser.add_argument('-i', '--input', type=str, action='store', help='Used to specify the input file. Otherwise the default urls.txt is used')
        parser.add_argument('-d', '--dir', type=str, action='store', help='Specify output directory for downloads')
        args=parser.parse_args()
        if args.input:
            self.in_file = args.input
        if args.dir:
            self.dir = args.dir
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def download(self):
        ''' download the files listed in the input file '''
        # setup URLs
        urls = []
        f = open(self.in_file,'r')
        for line in f.readlines():
            urls.append(line.strip())
        f.close()
        # setup download locations
        files = [url.split('/')[-1].strip() for url in urls]
        # create a thread for each url
        threads = []
        for f,url in zip(files,urls):
            filename = self.dir + '/' + f
            d = DownThread(url,filename)
            threads.append(d)
        for t in threads:
            t.start()
        for t in threads:
            t.join()

''' Use a thread to download one file given by url and stored in filename'''
class DownThread(threading.Thread):
    def __init__(self,url,filename):
        self.url = url
        self.filename = filename
        threading.Thread.__init__(self)
        self._content_consumed = False

    def run(self):
        print 'Downloading %s' % self.url
        r = requests.get(self.url, stream=True)
        with open(self.filename, 'wb') as f:
            for chunk in r.iter_content(10000):
                if not chunk:
                    break
                f.write(chunk)
                f.flush
 
if __name__ == '__main__':
    d = Downloader()
    d.download()
