#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys

from youtube_upload.main import upload_youtube_video, get_youtube_handler

from objects import MediaSource, MediaSource

from utils import Map

WATCH_VIDEO_URL = "https://www.youtube.com/watch?v={id}"

class Youtube():
    def __init__(self):
        super(Youtube, self).__init__()

    def upload(self, title, description, file_path):
        try:
            options = Map({
                "title": title,
                "description": description,
                "privacy": "public",
                "chunksize": 1024 * 1024 * 8
            })
            api = get_youtube_handler(options)

            video_id = upload_youtube_video(api, options, file_path, 1, 1)
            video_url = WATCH_VIDEO_URL.format(id=video_id)
            
            return video_url
        except Exception as e:
            raise e