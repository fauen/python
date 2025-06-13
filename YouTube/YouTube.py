from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

yd = yt.streams.filter(progressive=True).last()
yd.download('/Users/fauen/Movies')