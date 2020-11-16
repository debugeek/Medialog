#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os
import re
import requests
from pathlib import Path

from objects import MediaItem, MediaSource

HEADERS = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding":"deflate",
    "accept-language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    "cache-control":"no-cache",
    'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
}

class Downloader():
    def __init__(self):
        super(Downloader, self).__init__()
        self.headers = HEADERS
        self.session = requests.Session()

    def __download(self, item):
        Path(item.file_path).parent.mkdir(parents = True, exist_ok = True)

        if not os.path.exists(item.file_path):
            resp = self.session.get(item.url, timeout = 5, headers = self.headers)
            with open(item.file_path, 'wb') as fb:
                fb.write(resp.content)

    def download(self, item):
        try:
            return self.__download(item)
        except Exception as e:
            raise e
