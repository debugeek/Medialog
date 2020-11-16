#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os
import re
import requests

from objects import MediaItem, MediaSource
from downloader import Downloader

HEADERS = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding":"deflate",
    "accept-language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    "cache-control":"no-cache",
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
}

class Douyin():
    def __init__(self):
        super(Douyin, self).__init__()
        self.headers = HEADERS
        self.session = requests.Session()

    def __get_real_url(self, url):
        resp = self.session.get(url, timeout = 5, headers = self.headers)
        video_id = resp.url.split("/")[5]
        resp = self.session.get("https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + video_id, timeout = 5, headers = self.headers)
        video_url = re.findall(r'https://aweme.snssdk.com/aweme[\S]*?"', resp.text)[0][:-1]
        video_url = video_url.replace("/playwm/","/play/")
        return video_id, video_url

    def get(self, url):
        try:
            video_id, video_url = self.__get_real_url(url)

            if len(video_url) == 0:
                print("%s 下载失败" % video_id)
            else:
                item = MediaItem()
                item.source = MediaSource.Douyin
                item.file_path = '../downloads/douyin/%s.mp4' % (video_id)
                item.url = video_url

                downloader = Downloader()
                downloader.download(item)

                print("%s 下载完成" % video_id)

        except Exception as e:
            raise e