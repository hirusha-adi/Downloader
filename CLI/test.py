from pytube import *


yt = YouTube("https://www.youtube.com/watch?v=Jk1lkVYbZ_c")
# video = yt.streams.filter(progressive=True)
video = yt.streams.filter(file_extension="mp3")
print(video)

