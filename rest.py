#!/usr/bin/env python
from __future__ import print_function, absolute_import, division

import os
import logging
import requests

from sys import argv, exit
from time import time
from fuse import FUSE, Operations, LoggingMixIn

class Rest(LoggingMixIn, Operations):
    '''
    A simple REST API filesystem. Requires requests HTTP module.
    '''

    def __init__(self, host):
        self.host = host;

    def getattr(self, path, fh=None):
        # fake stat for now
        st = os.lstat('/tmp')
        if 'image/' in path:
            st = os.lstat('/tmp/file')

        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
            'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))

    def read(self, path, size, offset, fh):
        url = "%s/%s" % (self.host, path)
        r = requests.get(url)
        return r.json()

    def readdir(self, path, fh):
        url = "%s%s" % (self.host, path)
        url = url.rstrip('/')
        result = requests.get(url).json()
        return ['.', '..'] + [name.encode('utf-8')
                              for name in result['message']]

if __name__ == '__main__':
    if len(argv) != 3:
        print('usage: %s <api endpoint> <mountpoint>' % argv[0])
        exit(1)

    logging.basicConfig(level=logging.DEBUG)

    fuse = FUSE(Rest(argv[1]), argv[2], foreground=True, nothreads=True)

