#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os
import re
import time
import requests

from objects import MediaItem, MediaSource
from downloader import Downloader
from utils import MediaNameFormatter

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

class Ting55():
    def __init__(self):
        super(Ting55, self).__init__()
        self.headers = HEADERS
        self.session = requests.Session()

    def __get_chapter_info(self, book_id, chapter_number):
        url = 'https://m.ting55.com/book/%s-%d'%(book_id, chapter_number)
        resp = self.session.get(url, timeout = 5, headers = self.headers)
        xt = re.findall('meta name="_c" content="(.*?)"', resp.text)[0]
        chapter_name = re.findall('h1>(.*?)</h1>', resp.text)[0]
        chapter_name = MediaNameFormatter.formatted_file_name(chapter_name)
        return chapter_name, xt

    def __get_chapter_url(self, book_id, chapter_number, xt):
        url = 'https://m.ting55.com/book/%s-%d'%(book_id, chapter_number)
        data = {'bookId': book_id, 'isPay': 0, 'page': 1}

        headers = self.headers
        headers['xt'] = xt
        headers['Referer'] = url

        resp = self.session.post("https://m.ting55.com/glink", data = data, timeout = 5, headers = headers)
        url = resp.json()['ourl']
        return url

    def get(self, url):
        try:
            resp = self.session.get(url, timeout = 5, headers = self.headers)
            href = re.findall('<link rel="canonical" href="(.*?)"/>', resp.text)[0]
            book_id = re.findall('/book/(.*)', href)[0]
            book_name = re.findall('<h1>(.*?)</h1>',resp.text)[0]
            chapter_numbers = re.findall('<a class="f" href="/book', resp.text)

            for chapter_number in range(len(chapter_numbers)):
                chapter_number += 1

                chapter_name, xt = self.__get_chapter_info(book_id, chapter_number)
                file_path = '../downloads/ting55/%s/%s.mp4' % (book_name, chapter_name)

                if os.path.exists(file_path):
                    continue

                chapter_url = self.__get_chapter_url(book_id, chapter_number, xt)

                if len(chapter_url) == 0:
                    print("%s 下载失败" % chapter_name)
                else:
                    item = MediaItem()
                    item.source = MediaSource.Ting55
                    item.file_path = file_path
                    item.url = chapter_url

                    downloader = Downloader()
                    downloader.download(item)

                    print("%s 下载完成" % chapter_name)

                time.sleep(2)

        except Exception as e:
            raise e