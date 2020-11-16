#!/usr/bin/python 
# -*- coding: utf-8 -*-

from enum import Enum

class MediaSource(Enum):
    Unknown = 0

    Douyin = 2
    
    Ting55 = 48

class MediaItem():
    source = MediaSource.Unknown
    url = ""

    title = ""
    description = ""

    image = ""

    file_path = ""







