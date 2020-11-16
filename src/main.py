#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os
import sys
import optparse

from objects import MediaSource, MediaSource
from vendors.douyin import Douyin
from vendors.ting55 import Ting55
from vendors.youtube import Youtube

def main(arguments):
    usage = """Usage: %prog [options] url [url1 | url2 | ...]"""
    parser = optparse.OptionParser(usage)

    # Video metadata
    parser.add_option('-t', '--title', dest='title', type="string",
                      help='Media title')
    parser.add_option('-d', '--description', dest='description', type="string",
                      help='Media description')

    options, args = parser.parse_args(arguments)

    for idx, arg in enumerate(args):

        if 'douyin' in arg:
            douyin = Douyin()
            douyin.get(arg)
        elif 'ting55' in arg:
            ting55 = Ting55()
            ting55.get(arg)


if __name__ == '__main__':
    main(sys.argv[1:])
