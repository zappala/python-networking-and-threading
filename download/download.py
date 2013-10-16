import argparse
import os
import requests

''' Downloader for a set of files '''
class Downloader:
    def __init__(self):
        ''' initialize the file where the list of URLs is listed, and the
        directory where the downloads will be stored'''
        self.args = None
        self.parse_arguments()

    def parse_arguments(self):
        ''' parse arguments, which include '-i' for input file and
        '-d' for download directory'''
        parser = argparse.ArgumentParser(prog='Mass downloader', description='A simple script that downloads multiple files from a list of URLs specified in a file', add_help=True)
        parser.add_argument('-i', '--input', type=str, action='store', help='Specify the input file containing a list of URLs, default is urls.txt',default='urls.txt')
        parser.add_argument('-d', '--dir', type=str, action='store', help='Specify the directory where downloads are stored, default is downloads',default='downloads')
        args = parser.parse_args()
        self.in_file = args.input
        self.dir = args.dir
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def download(self):
        ''' download the files listed in the input file '''
        urls = []
        f = open(self.in_file,'r')
        for line in f.readlines():
            urls.append(line.strip())
        f.close()
        files = [url.split('/')[-1].strip() for url in urls]
        for f,url in zip(files,urls):
            filename = self.dir + '/' + f
            self.download_file(url,filename)
 
    def download_file(self,url,filename):
        ''' download one file given by url and stored in filename'''
        print 'Downloading %s' % url
        r = requests.get(url, stream=True)
        with open(filename, 'wb') as f:
            f.write(r.content)

 
if __name__ == '__main__':
    d = Downloader()
    d.download()
