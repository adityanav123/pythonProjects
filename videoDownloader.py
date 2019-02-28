import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

from pytube import YouTube
print('Enter a link : ')
link = input()
yt = YouTube(link)

print('Video Title : ', yt.title)
stream = yt.streams.first()
print("Stream selected : " , stream)
print('Video Size : ', convert_size(stream.filesize))


stream.download()
