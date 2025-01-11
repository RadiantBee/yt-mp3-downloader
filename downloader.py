#!/usr/bin/python
import yt_dlp as youtube_dl
import os

projPath = os.path.dirname(os.path.realpath(__file__))
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': projPath+'/music/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

urlfile = open("list", "r")

urls = list(filter(bool,urlfile.read().splitlines()))

for url in urls:
    if "&list" in url:
        url = url.split("&")[0]

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

