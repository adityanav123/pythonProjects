from pytube import YouTube
print('Enter a link : ')
link = input()
yt = YouTube(link)

print('Video Title : ', yt.title)

stream = yt.streams.first()

stream.download()
