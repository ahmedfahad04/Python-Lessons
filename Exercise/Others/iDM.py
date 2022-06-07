# import requests
# import time
#
# chunk_size = 256
#
# url = "https://secure.brightcove.com/services/mobile/streaming/index/master.m3u8?videoId=6208759178001&pubId=3588749423001&secure=true"
#
# r = requests.get(url, stream=True)
# #
# # with open("udemy.mp4", 'wb') as f:
# #     for chunk in r.iter_content(chunk_size=chunk_size):
# #         print(chunk)
# #         f.write(chunk)
# rp = requests.get(url)
# print(rp.text)
#
# from pytube import YouTube, version
# print(YouTube.__doc__)
# yt = YouTube(link)

# -*- coding: utf-8 -*-
"""
This module implements the core developer interface for pytube.

The problem domain of the :class:`YouTube <YouTube> class focuses almost
exclusively on the developer interface. Pytube offloads the heavy lifting to
smaller peripheral modules and functions.

"""
import re
from pytube.helpers import regex_search
def video_id(url: str) -> str:
    """Extract the ``video_id`` from a YouTube url.

    This function supports the following patterns:

    - :samp:`https://youtube.com/watch?v={video_id}`
    - :samp:`https://youtube.com/embed/{video_id}`
    - :samp:`https://youtu.be/{video_id}`

    :param str url:
        A YouTube url containing a video id.
    :rtype: str
    :returns:
        YouTube video id.
    """
    return regex_search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url, group=1)
print(video_id.__doc__)
print(video_id("https://www.youtube.com/watch?v=mRAkD4L8x80"))

print(help(filter))